#!/usr/bin/env python3
"""Paper XI third-model calibration probe.

This runner executes the c_fmt calibration suite described in:
  /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/infra/論文XI_第3モデル条件_実験計画書.md

It supports two modes:
  1. --dry-run: emit canonical expected responses and verify the scoring path.
  2. live execution: call an OpenAI or Anthropic model and write scored JSONL.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from collections import Counter
from pathlib import Path
from typing import Any

SUPPORTED_PROVIDERS = {"openai", "anthropic"}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def canonical_expected(record: dict[str, Any]) -> str:
    if record["kind"] == "json_ordered":
        return record["expected_canonical"]
    return record["expected_response"]


def resolve_output_file(
    output_file: Path,
    dry_run: bool,
    output_override: Path | None,
) -> Path:
    if output_override is not None:
        return output_override
    if dry_run:
        return output_file.with_name(f"{output_file.stem}_dry_run{output_file.suffix}")
    return output_file


def evaluate_response(record: dict[str, Any], response_text: str) -> dict[str, Any]:
    stripped = response_text.strip()
    if record["kind"] == "json_ordered":
        try:
            parsed = json.loads(stripped)
        except json.JSONDecodeError:
            return {"passed": False, "reason": "json_parse_error"}
        if not isinstance(parsed, dict):
            return {"passed": False, "reason": "json_not_object"}
        if list(parsed.keys()) != record["expected_key_order"]:
            return {
                "passed": False,
                "reason": "key_order_mismatch",
                "observed_key_order": list(parsed.keys()),
            }
        if parsed != record["expected_json"]:
            return {
                "passed": False,
                "reason": "json_value_mismatch",
                "observed_json": parsed,
            }
        return {"passed": True, "reason": "ok"}

    if stripped != record["expected_response"]:
        return {
            "passed": False,
            "reason": "literal_mismatch",
            "observed_response": stripped,
        }
    return {"passed": True, "reason": "ok"}


def call_openai(
    model: str,
    system_prompt: str,
    user_prompt: str,
    temperature: float,
    top_p: float,
    max_tokens: int,
) -> str:
    import openai

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")

    openai.api_key = api_key
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
    )
    content = response.choices[0].message.content
    return content if isinstance(content, str) else ""


def call_anthropic(
    model: str,
    system_prompt: str,
    user_prompt: str,
    temperature: float,
    top_p: float,
    max_tokens: int,
) -> str:
    from anthropic import Anthropic

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set")

    client = Anthropic(api_key=api_key)
    response = client.messages.create(
        model=model,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
    )
    chunks: list[str] = []
    for block in response.content:
        text = getattr(block, "text", None)
        if isinstance(text, str):
            chunks.append(text)
    return "".join(chunks)


def run_probe(
    manifest_path: Path,
    dry_run: bool,
    limit: int | None,
    sleep_seconds: float,
    output_override: Path | None,
) -> int:
    manifest = load_json(manifest_path)
    generation = manifest["generation"]
    candidate = manifest["m3_initial_candidate"]
    provider = candidate["provider"]
    model = candidate["model"]

    prompt_file = Path(manifest["calibration_suite"]["prompt_file"])
    output_file = resolve_output_file(
        Path(manifest["calibration_suite"]["output_file"]),
        dry_run=dry_run,
        output_override=output_override,
    )
    prompts = load_jsonl(prompt_file)
    if limit is not None:
        prompts = prompts[:limit]

    output_file.parent.mkdir(parents=True, exist_ok=True)

    block_counter: Counter[str] = Counter()
    pass_counter: Counter[str] = Counter()

    with output_file.open("w", encoding="utf-8") as handle:
        for record in prompts:
            if dry_run:
                response_text = canonical_expected(record)
            else:
                if provider == "openai":
                    response_text = call_openai(
                        model=model,
                        system_prompt=record["system_prompt"],
                        user_prompt=record["user_prompt"],
                        temperature=generation["temperature"],
                        top_p=generation["top_p"],
                        max_tokens=generation["max_tokens"],
                    )
                elif provider == "anthropic":
                    response_text = call_anthropic(
                        model=model,
                        system_prompt=record["system_prompt"],
                        user_prompt=record["user_prompt"],
                        temperature=generation["temperature"],
                        top_p=generation["top_p"],
                        max_tokens=generation["max_tokens"],
                    )
                else:
                    supported = ", ".join(sorted(SUPPORTED_PROVIDERS))
                    raise ValueError(
                        f"Unsupported provider: {provider}. "
                        f"Current runnable probe supports: {supported}"
                    )
                if sleep_seconds > 0:
                    time.sleep(sleep_seconds)

            verdict = evaluate_response(record, response_text)
            block = record["block"]
            block_counter[block] += 1
            if verdict["passed"]:
                pass_counter[block] += 1

            row = {
                "instance_id": record["instance_id"],
                "block": block,
                "provider": provider,
                "model": model,
                "dry_run": dry_run,
                "response_text": response_text,
                "verdict": verdict,
            }
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    total = sum(block_counter.values())
    passed = sum(pass_counter.values())
    print(f"probe={manifest['probe_name']}")
    print(f"provider={provider} model={model} dry_run={dry_run}")
    print(f"prompts={total} passed={passed} failed={total - passed}")
    for block in sorted(block_counter):
        print(
            f"block={block} passed={pass_counter[block]}/{block_counter[block]}"
        )
    print(f"output_file={output_file}")

    return 0 if passed == total else 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path(
            "/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/データ_3830.json"
        ),
        help="Path to the probe manifest JSON",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not call external APIs; emit canonical expected outputs instead.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional prompt limit for smoke tests.",
    )
    parser.add_argument(
        "--sleep-seconds",
        type=float,
        default=0.0,
        help="Optional sleep between live API calls.",
    )
    parser.add_argument(
        "--output-file",
        type=Path,
        default=None,
        help="Optional output path override. Dry-run defaults to a separate *_dry_run.jsonl file.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return run_probe(
        manifest_path=args.manifest,
        dry_run=args.dry_run,
        limit=args.limit,
        sleep_seconds=args.sleep_seconds,
        output_override=args.output_file,
    )


if __name__ == "__main__":
    sys.exit(main())
