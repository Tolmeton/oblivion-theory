from __future__ import annotations

try:
    import torch
except ImportError as exc:  # pragma: no cover - environment dependent
    raise SystemExit(
        "PyTorch is not installed in this environment. "
        "The demo is a real smoke test, so it stops here."
    ) from exc

from 忘却_変換器 import OblivionConfig, OblivionTransformer


def main() -> None:
    cfg = OblivionConfig(
        vocab_size=1024,
        dim=128,
        max_seq_len=64,
        max_loops=4,
        branch_count=6,
        keep_branches=2,
    )
    model = OblivionTransformer(cfg)
    input_ids = torch.randint(0, cfg.vocab_size, (2, 12))
    output = model(input_ids, return_state=True)

    print("logits:", tuple(output["logits"].shape))
    print("final_state:", tuple(output["final_state"].shape))
    print("loops_executed:", output["loops_executed"])
    print(
        "mean_cumulative_halt:",
        float(output["cumulative_halt"].mean().detach().cpu()),
    )


if __name__ == "__main__":
    main()
