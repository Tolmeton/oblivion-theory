from __future__ import annotations

from dataclasses import dataclass
from typing import Any

try:
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
except ImportError as exc:  # pragma: no cover - environment dependent
    torch = None
    nn = None
    F = None
    _TORCH_IMPORT_ERROR = exc
else:
    _TORCH_IMPORT_ERROR = None


def _raise_missing_torch() -> None:
    raise RuntimeError(
        "Oblivion Transformer v0.1 requires PyTorch. "
        "Install torch before importing or instantiating this module."
    ) from _TORCH_IMPORT_ERROR


@dataclass
class OblivionConfig:
    vocab_size: int = 32000
    dim: int = 256
    max_seq_len: int = 512
    max_loops: int = 6
    branch_count: int = 8
    keep_branches: int = 2
    mlp_multiplier: int = 4
    halt_threshold: float = 0.95
    dropout: float = 0.0


if nn is None:

    class SourceReservoir:
        def __init__(self, *_: Any, **__: Any) -> None:
            _raise_missing_torch()

    class FreedomExpander:
        def __init__(self, *_: Any, **__: Any) -> None:
            _raise_missing_torch()

    class OblivionProjector:
        def __init__(self, *_: Any, **__: Any) -> None:
            _raise_missing_torch()

    class SelfCompletionCore:
        def __init__(self, *_: Any, **__: Any) -> None:
            _raise_missing_torch()

    class KalonJudge:
        def __init__(self, *_: Any, **__: Any) -> None:
            _raise_missing_torch()

    class OblivionTransformer:
        def __init__(self, *_: Any, **__: Any) -> None:
            _raise_missing_torch()

else:

    class SourceReservoir(nn.Module):
        def __init__(self, cfg: OblivionConfig) -> None:
            super().__init__()
            self.embed = nn.Embedding(cfg.vocab_size, cfg.dim)
            self.anchor = nn.Sequential(
                nn.LayerNorm(cfg.dim),
                nn.Linear(cfg.dim, cfg.dim, bias=False),
                nn.Tanh(),
            )

        def forward(self, input_ids: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
            token_state = self.embed(input_ids)
            source_state = self.anchor(token_state)
            return token_state, source_state


    class FreedomExpander(nn.Module):
        def __init__(self, cfg: OblivionConfig) -> None:
            super().__init__()
            self.cfg = cfg
            self.pre = nn.Sequential(
                nn.LayerNorm(cfg.dim * 2),
                nn.Linear(cfg.dim * 2, cfg.dim * cfg.branch_count, bias=False),
                nn.GELU(),
            )
            self.branch_bias = nn.Embedding(cfg.branch_count, cfg.dim)

        def forward(
            self, core_state: torch.Tensor, source_state: torch.Tensor
        ) -> torch.Tensor:
            batch, seq, dim = core_state.shape
            mixed = torch.cat([core_state, source_state], dim=-1)
            branches = self.pre(mixed).view(batch, seq, self.cfg.branch_count, dim)
            branch_ids = torch.arange(
                self.cfg.branch_count, device=core_state.device, dtype=torch.long
            )
            return branches + self.branch_bias(branch_ids).view(
                1, 1, self.cfg.branch_count, dim
            )


    class OblivionProjector(nn.Module):
        def __init__(self, cfg: OblivionConfig) -> None:
            super().__init__()
            self.cfg = cfg
            self.scorer = nn.Sequential(
                nn.LayerNorm(cfg.dim * 2),
                nn.Linear(cfg.dim * 2, cfg.dim, bias=False),
                nn.GELU(),
                nn.Linear(cfg.dim, 1, bias=False),
            )

        def forward(
            self, branches: torch.Tensor, source_state: torch.Tensor
        ) -> tuple[torch.Tensor, dict[str, torch.Tensor]]:
            batch, seq, branch_count, dim = branches.shape
            source = source_state.unsqueeze(2).expand(batch, seq, branch_count, dim)
            score_input = torch.cat([branches, source], dim=-1)
            scores = self.scorer(score_input).squeeze(-1)

            keep_scores, keep_idx = scores.topk(self.cfg.keep_branches, dim=2)
            selected = torch.gather(
                branches,
                2,
                keep_idx.unsqueeze(-1).expand(batch, seq, self.cfg.keep_branches, dim),
            )

            keep_weights = F.softmax(keep_scores, dim=2)
            retained = (selected * keep_weights.unsqueeze(-1)).sum(dim=2)

            all_weights = F.softmax(scores, dim=2)
            kept_mass = torch.gather(all_weights, 2, keep_idx).sum(dim=2)
            forget_mass = 1.0 - kept_mass

            stats = {
                "scores": scores,
                "keep_idx": keep_idx,
                "keep_weights": keep_weights,
                "kept_mass": kept_mass,
                "forget_mass": forget_mass,
            }
            return retained, stats


    class SelfCompletionCore(nn.Module):
        def __init__(self, cfg: OblivionConfig) -> None:
            super().__init__()
            hidden = cfg.dim * cfg.mlp_multiplier
            self.repair = nn.Sequential(
                nn.LayerNorm(cfg.dim * 3 + 1),
                nn.Linear(cfg.dim * 3 + 1, hidden, bias=False),
                nn.GELU(),
                nn.Linear(hidden, cfg.dim, bias=False),
            )
            self.dropout = nn.Dropout(cfg.dropout)

        def forward(
            self,
            previous_core: torch.Tensor,
            retained_state: torch.Tensor,
            source_state: torch.Tensor,
            forget_mass: torch.Tensor,
        ) -> torch.Tensor:
            features = torch.cat(
                [
                    previous_core,
                    retained_state,
                    source_state,
                    forget_mass.unsqueeze(-1),
                ],
                dim=-1,
            )
            repaired = self.repair(features)
            return previous_core + self.dropout(repaired)


    class KalonJudge(nn.Module):
        def __init__(self, cfg: OblivionConfig) -> None:
            super().__init__()
            self.fidelity_head = nn.Linear(cfg.dim * 2, 1, bias=False)
            self.halt_head = nn.Linear(cfg.dim + 3, 1, bias=False)

        def forward(
            self,
            repaired_state: torch.Tensor,
            source_state: torch.Tensor,
            forget_mass: torch.Tensor,
        ) -> tuple[torch.Tensor, dict[str, torch.Tensor]]:
            fidelity = torch.sigmoid(
                self.fidelity_head(torch.cat([repaired_state, source_state], dim=-1))
            ).squeeze(-1)
            coherence = F.cosine_similarity(repaired_state, source_state, dim=-1)
            saturation = 1.0 - forget_mass

            halt_features = torch.cat(
                [
                    repaired_state,
                    fidelity.unsqueeze(-1),
                    coherence.unsqueeze(-1),
                    saturation.unsqueeze(-1),
                ],
                dim=-1,
            )
            halt_probability = torch.sigmoid(self.halt_head(halt_features)).squeeze(-1)
            metrics = {
                "fidelity": fidelity,
                "coherence": coherence,
                "saturation": saturation,
            }
            return halt_probability, metrics


    class OblivionTransformer(nn.Module):
        def __init__(self, cfg: OblivionConfig) -> None:
            super().__init__()
            self.cfg = cfg
            self.reservoir = SourceReservoir(cfg)
            self.expander = FreedomExpander(cfg)
            self.projector = OblivionProjector(cfg)
            self.repair = SelfCompletionCore(cfg)
            self.judge = KalonJudge(cfg)
            self.final_norm = nn.LayerNorm(cfg.dim)
            self.commit_head = nn.Linear(cfg.dim, cfg.vocab_size, bias=False)
            self.commit_head.weight = self.reservoir.embed.weight

        def forward(
            self,
            input_ids: torch.Tensor,
            n_loops: int | None = None,
            return_state: bool = False,
        ) -> torch.Tensor | dict[str, Any]:
            n_loops = n_loops or self.cfg.max_loops

            core_state, source_state = self.reservoir(input_ids)
            accumulated = torch.zeros_like(core_state)
            cumulative_halt = torch.zeros(
                core_state.shape[:2], device=core_state.device, dtype=core_state.dtype
            )
            loop_records: list[dict[str, torch.Tensor]] = []

            for loop_idx in range(n_loops):
                branches = self.expander(core_state, source_state)
                retained_state, projection = self.projector(branches, source_state)
                repaired_state = self.repair(
                    core_state,
                    retained_state,
                    source_state,
                    projection["forget_mass"],
                )
                halt_probability, judge_metrics = self.judge(
                    repaired_state, source_state, projection["forget_mass"]
                )

                remaining = (1.0 - cumulative_halt).clamp(min=0.0)
                weight = torch.where(
                    cumulative_halt + halt_probability >= self.cfg.halt_threshold,
                    remaining,
                    halt_probability,
                )
                accumulated = accumulated + repaired_state * weight.unsqueeze(-1)
                cumulative_halt = cumulative_halt + weight
                core_state = repaired_state

                loop_records.append(
                    {
                        "loop_idx": torch.tensor(loop_idx, device=core_state.device),
                        "forget_mass": projection["forget_mass"],
                        "kept_mass": projection["kept_mass"],
                        "halt_probability": halt_probability,
                        "fidelity": judge_metrics["fidelity"],
                        "coherence": judge_metrics["coherence"],
                    }
                )

                if bool((cumulative_halt >= self.cfg.halt_threshold).all()):
                    break

            final_state = torch.where(
                cumulative_halt.unsqueeze(-1) > 0,
                accumulated,
                core_state,
            )
            logits = self.commit_head(self.final_norm(final_state))

            if not return_state:
                return logits

            return {
                "logits": logits,
                "source_state": source_state,
                "final_state": final_state,
                "cumulative_halt": cumulative_halt,
                "loops_executed": len(loop_records),
                "loop_records": loop_records,
            }


__all__ = [
    "OblivionConfig",
    "SourceReservoir",
    "FreedomExpander",
    "OblivionProjector",
    "SelfCompletionCore",
    "KalonJudge",
    "OblivionTransformer",
]
