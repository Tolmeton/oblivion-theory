#!/usr/bin/env python3
"""Run the Paper XI H3 one-task A/B smoke.

This runner executes exactly one task, one provider family, two conditions,
and one repeat. It writes JSONL and performs no judging. The goal is to test
the generation pipe before scaling the clean-room MVP.
"""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path
from typing import Any


SUPPORTED_PROVIDERS = {"openai", "anthropic"}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require_api_key(provider: str) -> None:
    env_name = {
        "openai": "OPENAI_API_KEY",
        "anthropic": "ANTHROPIC_API_KEY",
    }[provider]
    if not os.environ.get(env_name):
        raise RuntimeError(f"{env_name} is not set")


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
    model = model_override or candidate["model"]
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
            if provider == "openai":
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
        default=Path("/home/makaron8426/Sync/oikos/oblivion-theory/experiments/paper_xi_h3_smoke_manifest.json"),
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
