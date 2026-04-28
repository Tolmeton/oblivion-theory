#!/usr/bin/env python3
"""Run the Paper XI H3 one-task A/B smoke.

This runner executes exactly one task, one provider family, two conditions,
and one repeat. It writes JSONL and performs no judging. The control plane is
CLI-only; NVIDIA NIM and Google Vertex are allowed as backend APIs.
"""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path
from typing import Any


SUPPORTED_PROVIDERS = {"nvidia", "vertex", "openai", "anthropic"}
SELECT_BEFORE_RUN_MARKERS = {
    "select_before_run",
    "select_before_run_or_set_NVIDIA_MODEL",
    "select_before_run_or_set_VERTEX_MODEL",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require_api_key(provider: str) -> None:
    env_name = {
        "nvidia": "NVIDIA_API_KEY",
        "vertex": "GOOGLE_CLOUD_PROJECT",
        "openai": "OPENAI_API_KEY",
        "anthropic": "ANTHROPIC_API_KEY",
    }[provider]
    if not os.environ.get(env_name):
        raise RuntimeError(f"{env_name} is not set")
    if provider == "vertex" and not os.environ.get("GOOGLE_CLOUD_LOCATION"):
        raise RuntimeError("GOOGLE_CLOUD_LOCATION is not set")


def resolve_model(provider: str, model_override: str | None, candidate_model: str) -> str:
    if model_override:
        return model_override

    env_candidates = [
        "PAPER_XI_H3_MODEL",
        {
            "nvidia": "NVIDIA_MODEL",
            "vertex": "VERTEX_MODEL",
            "openai": "OPENAI_MODEL",
            "anthropic": "ANTHROPIC_MODEL",
        }[provider],
    ]
    for env_name in env_candidates:
        value = os.environ.get(env_name)
        if value:
            return value

    if candidate_model not in SELECT_BEFORE_RUN_MARKERS:
        return candidate_model

    raise RuntimeError(
        f"model is not set for provider={provider}; pass --model or set "
        f"PAPER_XI_H3_MODEL / {env_candidates[-1]}"
    )


def call_nvidia(model: str, prompt: str, generation: dict[str, Any]) -> str:
    from openai import OpenAI

    base_url = os.environ.get("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
    client = OpenAI(base_url=base_url, api_key=os.environ["NVIDIA_API_KEY"])
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=generation["temperature"],
        top_p=generation["top_p"],
        max_tokens=generation["max_tokens"],
    )
    content = response.choices[0].message.content
    return content if isinstance(content, str) else ""


def call_vertex(model: str, prompt: str, generation: dict[str, Any]) -> str:
    from google import genai
    from google.genai.types import GenerateContentConfig

    client = genai.Client(
        vertexai=True,
        project=os.environ["GOOGLE_CLOUD_PROJECT"],
        location=os.environ["GOOGLE_CLOUD_LOCATION"],
    )
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=GenerateContentConfig(
            temperature=generation["temperature"],
            top_p=generation["top_p"],
            max_output_tokens=generation["max_tokens"],
        ),
    )
    text = getattr(response, "text", None)
    return text if isinstance(text, str) else ""


def call_openai(model: str, prompt: str, generation: dict[str, Any]) -> str:
    from openai import OpenAI

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=generation["temperature"],
        top_p=generation["top_p"],
        max_tokens=generation["max_tokens"],
    )
    content = response.choices[0].message.content
    return content if isinstance(content, str) else ""


def call_anthropic(model: str, prompt: str, generation: dict[str, Any]) -> str:
    from anthropic import Anthropic

    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    response = client.messages.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=generation["temperature"],
        top_p=generation["top_p"],
        max_tokens=generation["max_tokens"],
    )
    chunks: list[str] = []
    for block in response.content:
        text = getattr(block, "text", None)
        if isinstance(text, str):
            chunks.append(text)
    return "".join(chunks)


def required_sections_present(response_text: str) -> bool:
    lowered = response_text.lower()
    return all(
        section in lowered
        for section in ["answer", "reasons", "uncertainty", "failure condition"]
    )


def smoke_rows(packet: dict[str, Any]) -> list[dict[str, str]]:
    return [
        {
            "condition": "A",
            "encoding": packet["condition_a"]["encoding"],
            "prompt": packet["condition_a"]["prompt"],
        },
        {
            "condition": "B",
            "encoding": packet["condition_b"]["encoding"],
            "prompt": packet["condition_b"]["prompt"],
        },
    ]


def run(
    manifest_path: Path,
    provider_override: str | None,
    model_override: str | None,
    output_override: Path | None,
    sleep_seconds: float,
) -> int:
    manifest = load_json(manifest_path)
    packet = load_json(Path(manifest["dry_run_packet"]))
    generation = manifest["generation_contract"]
    candidate = manifest["provider_candidate"]
    provider = provider_override or candidate["provider"]
    model = resolve_model(provider, model_override, candidate["model"])
    output_file = output_override or Path(manifest["output_file"])

    if provider not in SUPPORTED_PROVIDERS:
        supported = ", ".join(sorted(SUPPORTED_PROVIDERS))
        raise ValueError(f"Unsupported provider {provider}; supported providers: {supported}")

    require_api_key(provider)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    rows_written = 0
    failures = 0
    with output_file.open("w", encoding="utf-8") as handle:
        for row in smoke_rows(packet):
            started_at = time.time()
            if provider == "nvidia":
                response_text = call_nvidia(model, row["prompt"], generation)
            elif provider == "vertex":
                response_text = call_vertex(model, row["prompt"], generation)
            elif provider == "openai":
                response_text = call_openai(model, row["prompt"], generation)
            else:
                response_text = call_anthropic(model, row["prompt"], generation)
            elapsed_seconds = time.time() - started_at

            verdict = {
                "nonempty": bool(response_text.strip()),
                "required_sections_present": required_sections_present(response_text),
            }
            if not all(verdict.values()):
                failures += 1

            output_row = {
                "manifest": manifest["manifest_name"],
                "task_id": packet["task_id"],
                "input_id": packet["input_id"],
                "condition": row["condition"],
                "encoding": row["encoding"],
                "provider": provider,
                "model": model,
                "repeat": 1,
                "temperature": generation["temperature"],
                "top_p": generation["top_p"],
                "max_tokens": generation["max_tokens"],
                "control_plane": "cli",
                "elapsed_seconds": round(elapsed_seconds, 3),
                "prompt": row["prompt"],
                "response_text": response_text,
                "smoke_verdict": verdict,
            }
            handle.write(json.dumps(output_row, ensure_ascii=False) + "\n")
            rows_written += 1

            if sleep_seconds > 0:
                time.sleep(sleep_seconds)

    print(f"manifest={manifest['manifest_name']}")
    print(f"provider={provider} model={model}")
    print(f"rows={rows_written} failures={failures}")
    print(f"output_file={output_file}")
    return 0 if failures == 0 else 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/paper_xi_h3_smoke_manifest.json"),
    )
    parser.add_argument("--provider", choices=sorted(SUPPORTED_PROVIDERS), default=None)
    parser.add_argument("--model", default=None)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--sleep-seconds", type=float, default=0.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        return run(
            manifest_path=args.manifest,
            provider_override=args.provider,
            model_override=args.model,
            output_override=args.output,
            sleep_seconds=args.sleep_seconds,
        )
    except RuntimeError as exc:
        print(f"BLOCKED: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
