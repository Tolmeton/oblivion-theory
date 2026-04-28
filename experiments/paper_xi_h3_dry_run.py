#!/usr/bin/env python3
"""Materialize a Paper XI H3 clean-room A/B dry-run packet.

This script does not call model APIs. It verifies the prompt-pair skeleton,
injects one fixed input, and writes the exact prompts that a live runner would
send for the selected task.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REQUIRED_RECORD_KEYS = {
    "task_id",
    "domain",
    "task_type",
    "task",
    "condition_a_prompt",
    "condition_b_prompt",
    "c_e_audit",
}

REQUIRED_AUDIT = {
    "goal": "fixed",
    "procedure": "fixed",
    "constraints": "fixed",
    "output_schema": "fixed",
    "notation": "changed",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.strip()
        if not stripped:
            continue
        try:
            rows.append(json.loads(stripped))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSONL") from exc
    return rows


def find_one(rows: list[dict[str, Any]], key: str, value: str) -> dict[str, Any]:
    matches = [row for row in rows if row.get(key) == value]
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one row where {key}={value}, found {len(matches)}")
    return matches[0]


def validate_pair(record: dict[str, Any]) -> dict[str, bool]:
    missing = REQUIRED_RECORD_KEYS - set(record)
    if missing:
        raise ValueError(f"{record.get('task_id', '<unknown>')}: missing keys {sorted(missing)}")

    audit = record["c_e_audit"]
    for key, expected in REQUIRED_AUDIT.items():
        observed = audit.get(key)
        if observed != expected:
            raise ValueError(
                f"{record['task_id']}: c_e_audit.{key} must be {expected}, observed {observed}"
            )

    task = record["task"]
    return {
        "condition_a_contains_task": task in record["condition_a_prompt"],
        "condition_b_contains_task": task in record["condition_b_prompt"],
        "condition_a_has_input_slot": "{INPUT}" in record["condition_a_prompt"],
        "condition_b_has_input_slot": "{INPUT}" in record["condition_b_prompt"],
    }


def materialize_prompt(template: str, input_text: str) -> str:
    prompt = template.replace("{INPUT}", input_text)
    if "{INPUT}" in prompt:
        raise ValueError("unfilled {INPUT} slot remains")
    return prompt


def run(manifest_path: Path, task_id: str | None, input_id: str | None, output: Path | None) -> int:
    manifest = load_json(manifest_path)
    files = manifest["files"]
    dry_run = manifest["dry_run"]

    selected_task_id = task_id or dry_run["task_id"]
    selected_input_id = input_id or dry_run["input_id"]
    output_path = output or Path(dry_run["expected_output"])

    prompt_pairs = load_jsonl(Path(files["prompt_pairs"]))
    dry_run_inputs = load_jsonl(Path(files["dry_run_inputs"]))

    if len(prompt_pairs) != manifest["mvp_scope"]["task_count"]:
        raise ValueError(
            f"prompt pair count mismatch: expected {manifest['mvp_scope']['task_count']}, "
            f"observed {len(prompt_pairs)}"
        )

    record = find_one(prompt_pairs, "task_id", selected_task_id)
    input_record = find_one(dry_run_inputs, "input_id", selected_input_id)
    if input_record["task_id"] != selected_task_id:
        raise ValueError(
            f"input task mismatch: input has {input_record['task_id']}, selected {selected_task_id}"
        )

    checks = validate_pair(record)
    if not all(checks.values()):
        failed = [key for key, value in checks.items() if not value]
        raise ValueError(f"{selected_task_id}: failed checks {failed}")

    input_text = input_record["input_text"]
    prompt_a = materialize_prompt(record["condition_a_prompt"], input_text)
    prompt_b = materialize_prompt(record["condition_b_prompt"], input_text)

    packet = {
        "manifest": manifest["manifest_name"],
        "dry_run": True,
        "api_calls": "forbidden",
        "task_id": selected_task_id,
        "input_id": selected_input_id,
        "domain": record["domain"],
        "task_type": record["task_type"],
        "task": record["task"],
        "checks": {
            **checks,
            "prompt_pair_count": len(prompt_pairs),
            "condition_a_unfilled_input": "{INPUT}" in prompt_a,
            "condition_b_unfilled_input": "{INPUT}" in prompt_b,
        },
        "condition_a": {
            "condition": "A",
            "encoding": "natural_language",
            "prompt": prompt_a,
        },
        "condition_b": {
            "condition": "B",
            "encoding": "structural_notation",
            "prompt": prompt_b,
        },
        "judge_rubric": files["judge_rubric"],
        "c_e_audit": record["c_e_audit"],
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"manifest={manifest['manifest_name']}")
    print(f"task_id={selected_task_id} input_id={selected_input_id}")
    print(f"prompt_pairs={len(prompt_pairs)} dry_run=True api_calls=forbidden")
    print(f"output_file={output_path}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("/home/makaron8426/Sync/oikos/oblivion-theory/experiments/paper_xi_h3_clean_room_manifest.json"),
    )
    parser.add_argument("--task-id", default=None)
    parser.add_argument("--input-id", default=None)
    parser.add_argument("--output", type=Path, default=None)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return run(args.manifest, args.task_id, args.input_id, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
