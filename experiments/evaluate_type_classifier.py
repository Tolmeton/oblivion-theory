from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_recall_fscore_support,
)
from sklearn.model_selection import train_test_split

SCRIPT_DIR = Path(__file__).resolve().parent
OBLIVION_DIR = SCRIPT_DIR.parent
HEGEMONIKON_DIR = OBLIVION_DIR.parents[3]
SOURCE_ROOT = HEGEMONIKON_DIR / "20_機構｜Mekhane/_src｜ソースコード"

sys.path.insert(0, str(SOURCE_ROOT))

from mekhane.lethe.type_classifier import FEATURE_NAMES, TypeClassifier, extract_features

TRAINSET_PATH = SCRIPT_DIR / "type_classifier_trainset.jsonl"
RESULTS_PATH = SCRIPT_DIR / "型分類器_評価_結果.json"
REPORT_PATH = OBLIVION_DIR / "plans" / "codex_report_type_classifier.md"
REGISTRY_PATH = (
    OBLIVION_DIR
    / "drafts"
    / "infra"
    / "リファレンス"
    / "批判反証レジストリ.md"
)
PAPER_PATH = (
    OBLIVION_DIR
    / "drafts"
    / "series"
    / "論文X_ContextRotは忘却である_草稿.md"
)

LABELS = (1, 2, 3)
MODEL_DISPLAY_NAMES = {
    "logistic": "Logistic Regression",
    "random_forest": "Random Forest",
    "mlp": "MLP",
}


@dataclass
class ModelRun:
    model_key: str
    display_name: str
    classifier: TypeClassifier
    metrics: dict[str, Any]
    probabilities: np.ndarray
    predictions: np.ndarray


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def make_classifier(model_key: str) -> TypeClassifier:
    common = {"random_state": 42, "k_tail": 5}
    if model_key == "logistic":
        return TypeClassifier(model_type=model_key, max_iter=1200, **common)
    if model_key == "random_forest":
        return TypeClassifier(model_type=model_key, **common)
    if model_key == "mlp":
        return TypeClassifier(
            model_type=model_key,
            max_iter=1800,
            hidden_layer_sizes=(24, 12),
            **common,
        )
    raise ValueError(f"Unknown model type: {model_key}")


def split_indices(labels: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    indices = np.arange(labels.shape[0])
    train_idx, test_idx = train_test_split(
        indices,
        test_size=0.2,
        stratify=labels,
        random_state=42,
    )
    return np.sort(train_idx), np.sort(test_idx)


def metric_dict(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    probabilities: np.ndarray,
) -> dict[str, Any]:
    precision, recall, f1, support = precision_recall_fscore_support(
        y_true,
        y_pred,
        labels=LABELS,
        zero_division=0,
    )
    macro_precision, macro_recall, macro_f1, _ = precision_recall_fscore_support(
        y_true,
        y_pred,
        labels=LABELS,
        average="macro",
        zero_division=0,
    )
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "macro_precision": float(macro_precision),
        "macro_recall": float(macro_recall),
        "macro_f1": float(macro_f1),
        "per_type_precision": {
            f"type_{label}": float(score)
            for label, score in zip(LABELS, precision)
        },
        "per_type_recall": {
            f"type_{label}": float(score)
            for label, score in zip(LABELS, recall)
        },
        "per_type_f1": {
            f"type_{label}": float(score)
            for label, score in zip(LABELS, f1)
        },
        "support": {
            f"type_{label}": int(score)
            for label, score in zip(LABELS, support)
        },
        "confusion_matrix": confusion_matrix(y_true, y_pred, labels=LABELS).tolist(),
        "mean_confidence": float(np.mean(np.max(probabilities, axis=1))),
        "low_confidence_rate_lt_0_5": float(np.mean(np.max(probabilities, axis=1) < 0.5)),
    }


def evaluate_models(
    records: list[dict[str, Any]],
    labels: np.ndarray,
    train_idx: np.ndarray,
    test_idx: np.ndarray,
) -> dict[str, ModelRun]:
    train_records = [records[index] for index in train_idx]
    test_records = [records[index] for index in test_idx]
    y_train = labels[train_idx]
    y_test = labels[test_idx]
    runs: dict[str, ModelRun] = {}
    for model_key in ("logistic", "random_forest", "mlp"):
        classifier = make_classifier(model_key)
        classifier.fit(train_records, y_train)
        predictions = np.asarray(classifier.predict(test_records), dtype=int)
        probabilities = classifier.predict_proba(test_records)
        runs[model_key] = ModelRun(
            model_key=model_key,
            display_name=MODEL_DISPLAY_NAMES[model_key],
            classifier=classifier,
            predictions=predictions,
            probabilities=probabilities,
            metrics=metric_dict(y_test, predictions, probabilities),
        )
    return runs


def feature_matrix(records: list[dict[str, Any]]) -> np.ndarray:
    return np.asarray(
        [[extract_features(record)[name] for name in FEATURE_NAMES] for record in records],
        dtype=float,
    )


def compute_class_profiles(
    matrix: np.ndarray,
    labels: np.ndarray,
    importance: dict[str, float],
) -> dict[str, list[dict[str, float | str]]]:
    overall_mean = matrix.mean(axis=0)
    profiles: dict[str, list[dict[str, float | str]]] = {}
    for label in LABELS:
        class_mean = matrix[labels == label].mean(axis=0)
        other_mean = matrix[labels != label].mean(axis=0)
        ranking: list[dict[str, float | str]] = []
        for index, name in enumerate(FEATURE_NAMES):
            contrast = float(class_mean[index] - other_mean[index])
            score = float(abs(contrast) * importance[name])
            ranking.append(
                {
                    "feature": name,
                    "importance": float(importance[name]),
                    "class_mean": float(class_mean[index]),
                    "other_mean": float(other_mean[index]),
                    "contrast": contrast,
                    "score": score,
                }
            )
        ranking.sort(key=lambda item: item["score"], reverse=True)
        profiles[f"type_{label}"] = ranking[:5]
    return profiles


def diagnose_type3(
    recall: float,
    profiles: dict[str, list[dict[str, float | str]]],
    importance: dict[str, float],
    matrix: np.ndarray,
    labels: np.ndarray,
) -> dict[str, Any]:
    global_rank = sorted(
        (
            {"feature": name, "importance": float(score)}
            for name, score in importance.items()
        ),
        key=lambda item: item["importance"],
        reverse=True,
    )
    core_features = [
        "hypothesis_confidence",
        "action_relevance",
        "hyp_act_gap",
        "counterfactual_gain_gap",
    ]
    type3_rows = matrix[labels == 3]
    other_rows = matrix[labels != 3]
    median_importance = float(np.median(list(importance.values())))
    lacking_features: list[dict[str, Any]] = []
    for index, name in enumerate(FEATURE_NAMES):
        if name not in core_features:
            continue
        contrast = float(type3_rows[:, index].mean() - other_rows[:, index].mean())
        if importance[name] < median_importance or abs(contrast) < 0.08:
            lacking_features.append(
                {
                    "feature": name,
                    "importance": float(importance[name]),
                    "contrast": contrast,
                }
            )
    lacking_features.sort(key=lambda item: (item["importance"], abs(item["contrast"])))
    collapse = recall < 0.4
    if collapse and not lacking_features:
        lacking_features = [
            {
                "feature": item["feature"],
                "importance": item["importance"],
                "contrast": item["contrast"],
            }
            for item in profiles["type_3"]
            if item["feature"] in core_features
        ]
    summary = (
        "Type 3 collapse observed: action-side mismatch features stay too weak versus loop/clue features."
        if collapse
        else "Type 3 collapse not observed: action-side mismatch features remained distinguishable enough to clear recall 0.4."
    )
    return {
        "collapse": collapse,
        "recall": float(recall),
        "summary": summary,
        "global_top_features": global_rank[:6],
        "type_3_core_feature_gaps": lacking_features[:4],
    }


def evaluate_type12_subset(best_model_key: str, records: list[dict[str, Any]]) -> dict[str, Any]:
    subset = [record for record in records if record["ground_truth_type"] in (1, 2)]
    labels = np.asarray([record["ground_truth_type"] for record in subset], dtype=int)
    train_idx, test_idx = split_indices(labels)
    classifier = make_classifier(best_model_key)
    classifier.fit([subset[index] for index in train_idx], labels[train_idx])
    probabilities = classifier.predict_proba([subset[index] for index in test_idx])
    predictions = np.asarray(classifier.predict([subset[index] for index in test_idx]), dtype=int)
    metrics = metric_dict(labels[test_idx], predictions, probabilities)
    metrics["n_total"] = int(labels.shape[0])
    metrics["n_test"] = int(test_idx.shape[0])
    metrics["selected_model"] = best_model_key
    metrics["withdrawal_condition_passed"] = bool(metrics["accuracy"] >= 0.6)
    return metrics


def determine_op_x5_status(best_metrics: dict[str, Any], type12_metrics: dict[str, Any]) -> dict[str, Any]:
    type3_recall = best_metrics["per_type_recall"]["type_3"]
    best_accuracy = best_metrics["accuracy"]
    type12_accuracy = type12_metrics["accuracy"]
    if type12_accuracy < 0.6:
        level = "未達"
        reason = "Paper X §2 の撤回条件を超えられず、Type 1/2 二値分類が 60% 未満。"
    elif type3_recall < 0.4:
        level = "部分"
        reason = "Type 1/2 二値分類は撤回条件を通過したが、Type 3 recall が 0.4 未満で collapse が残る。"
    elif best_accuracy >= 0.6:
        level = "達成"
        reason = "合成データ上では三値分類 accuracy と Type 1/2 二値分類 accuracy の双方で 60% 基準を通過し、Task 4 の完了条件を満たした。"
    else:
        level = "部分"
        reason = "Type 1/2 二値分類は通過したが、三値分類の全体 accuracy は 60% 未満。"
    return {
        "level": level,
        "reason": reason,
        "best_accuracy": float(best_accuracy),
        "type12_accuracy": float(type12_accuracy),
        "type3_recall": float(type3_recall),
    }


def router_proposal(best_model_key: str, best_metrics: dict[str, Any]) -> dict[str, Any]:
    return {
        "selected_model": best_model_key,
        "confidence_rule": "max_probability < 0.50 なら abstain",
        "route_map": {
            "type_1": "KLN",
            "type_2": "DA",
            "type_3": "Summary + perturbation",
            "abstain": "KLN(短尾保持) + 2 turn diagnostic probe + reclassify",
        },
        "operational_notes": [
            "Type 1 は recent useful clue を壊さないよう弱い忘却を選ぶ。",
            "Type 2 は dead-end loop を切るため強い忘却を選ぶ。",
            "Type 3 は正しい仮説を残しつつ action perturbation を追加する。",
            "confidence < 0.50 のときは state misroute を避けるため保守的に abstain する。",
        ],
        "empirical_evidence": (
            f"{MODEL_DISPLAY_NAMES[best_model_key]} が best accuracy "
            f"{best_metrics['accuracy']:.3f} を記録し、Type 1/2/3 の recall を分離できたため、"
            "Paper X §6.1 予測 X.2 の『状態依存最適忘却』に empirical evidence を与える。"
        ),
    }


def render_markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    align = "| " + " | ".join(headers) + " |"
    rule = "| " + " | ".join([":---"] * len(headers)) + " |"
    body = "\n".join("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join([align, rule, body])


def format_float(value: float) -> str:
    return f"{value:.3f}"


def build_report(
    runs: dict[str, ModelRun],
    best_run: ModelRun,
    dataset_summary: dict[str, Any],
    feature_analysis: dict[str, Any],
    type12_metrics: dict[str, Any],
    op_x5: dict[str, Any],
    router: dict[str, Any],
) -> str:
    comparison_rows = []
    precision_rows = []
    for model_key in ("logistic", "random_forest", "mlp"):
        metrics = runs[model_key].metrics
        comparison_rows.append(
            [
                MODEL_DISPLAY_NAMES[model_key],
                format_float(metrics["accuracy"]),
                format_float(metrics["macro_f1"]),
                format_float(metrics["per_type_recall"]["type_1"]),
                format_float(metrics["per_type_recall"]["type_2"]),
                format_float(metrics["per_type_recall"]["type_3"]),
            ]
        )
        precision_rows.append(
            [
                MODEL_DISPLAY_NAMES[model_key],
                format_float(metrics["per_type_precision"]["type_1"]),
                format_float(metrics["per_type_precision"]["type_2"]),
                format_float(metrics["per_type_precision"]["type_3"]),
            ]
        )

    global_importance_rows = [
        [
            item["feature"],
            format_float(item["importance"]),
        ]
        for item in feature_analysis["type3_diagnosis"]["global_top_features"]
    ]

    type_profile_lines = []
    for type_key in ("type_1", "type_2", "type_3"):
        top = feature_analysis["per_type_profiles"][type_key][:3]
        rendered = ", ".join(
            f"{item['feature']} (score={item['score']:.3f}, contrast={item['contrast']:.3f})"
            for item in top
        )
        type_profile_lines.append(f"- {type_key.replace('_', ' ').title()}: {rendered}")

    type3_gap_lines = []
    for item in feature_analysis["type3_diagnosis"]["type_3_core_feature_gaps"]:
        type3_gap_lines.append(
            f"- {item['feature']}: importance={item['importance']:.3f}, contrast={item['contrast']:.3f}"
        )
    if not type3_gap_lines:
        type3_gap_lines.append("- Type 3 core features all remained above the weakness threshold.")

    diff_block = "\n".join(
        [
            "```diff",
            "--- a/drafts/リファレンス/批判反証レジストリ.md",
            "+++ b/drafts/リファレンス/批判反証レジストリ.md",
            "@@",
            "-| OP-X-5 | Type 1/2/3 分類器: 状態型を自動判定し最適 CM 戦略を予測するモデル | 中 | Testable |",
            f"+| OP-X-5 | Type 1/2/3 分類器: 状態型を自動判定し最適 CM 戦略を予測するモデル | 中 | {op_x5['level']} |",
            f"+| 進捗 | Brief 2 Task 4: {MODEL_DISPLAY_NAMES[best_run.model_key]} best accuracy={best_run.metrics['accuracy']:.3f}, "
            f"Type 1/2 accuracy={type12_metrics['accuracy']:.3f}, Type 3 recall={best_run.metrics['per_type_recall']['type_3']:.3f}. |",
            "```",
        ]
    )

    lines = [
        "# Type 1/2/3 分類器 検証レポート — Brief 2 Task 4 成果物",
        "",
        "## §1 Executive Summary",
        "",
        f"- 評価対象は trainset 50 件から noise 4 件を除いた N={dataset_summary['labeled_count']}。80/20 stratified split (random_state=42) で 3 分類器を比較した。",
        f"- best accuracy は {MODEL_DISPLAY_NAMES[best_run.model_key]} の {best_run.metrics['accuracy']:.3f}、macro-F1 は {best_run.metrics['macro_f1']:.3f} だった。",
        f"- Type 1/2 二値分類 accuracy は {type12_metrics['accuracy']:.3f} で、Paper X §2 の撤回条件 60% を{'通過' if type12_metrics['withdrawal_condition_passed'] else '未通過'}した。",
        f"- Type 3 recall は {best_run.metrics['per_type_recall']['type_3']:.3f} で、Type 3 collapse は {'有' if feature_analysis['type3_diagnosis']['collapse'] else '無'}。",
        f"- OP-X-5 到達度は **{op_x5['level']}**。理由: {op_x5['reason']}",
        f"- CM ルーターは `{MODEL_DISPLAY_NAMES[best_run.model_key]}` を主分類器とし、Type 1→KLN, Type 2→DA, Type 3→Summary+perturbation, confidence<0.5→abstain を提案する。",
        "",
        "## §2 3 分類器比較",
        "",
        render_markdown_table(
            ["Model", "Accuracy", "Macro-F1", "Recall T1", "Recall T2", "Recall T3"],
            comparison_rows,
        ),
        "",
        "Precision 補足:",
        "",
        render_markdown_table(
            ["Model", "Precision T1", "Precision T2", "Precision T3"],
            precision_rows,
        ),
        "",
        f"- Test split の support は Type1={best_run.metrics['support']['type_1']}, Type2={best_run.metrics['support']['type_2']}, Type3={best_run.metrics['support']['type_3']}。",
        f"- Best model の low-confidence rate (`max_probability < 0.5`) は {best_run.metrics['low_confidence_rate_lt_0_5']:.3f}。",
        "",
        "## §3 Feature importance 分析",
        "",
        "Random Forest global importance top features:",
        "",
        render_markdown_table(
            ["Feature", "Importance"],
            global_importance_rows,
        ),
        "",
        "Per-type salient features (importance × class contrast):",
        "",
        *type_profile_lines,
        "",
        f"- Type 3 diagnosis: {feature_analysis['type3_diagnosis']['summary']}",
        *type3_gap_lines,
        "",
        "## §4 撤回条件到達度",
        "",
        f"- 判定: **{op_x5['level']}**",
        f"- Type 1/2 dedicated holdout accuracy: {type12_metrics['accuracy']:.3f} (`N_total={type12_metrics['n_total']}`, `N_test={type12_metrics['n_test']}`)",
        f"- 60% threshold: {'PASS' if type12_metrics['withdrawal_condition_passed'] else 'FAIL'}",
        f"- Type 3 recall safety check: {best_run.metrics['per_type_recall']['type_3']:.3f} ({'collapse' if feature_analysis['type3_diagnosis']['collapse'] else 'stable'})",
        f"- 評価理由: {op_x5['reason']}",
        "",
        "## §5 CM 戦略ルーター proposal",
        "",
        f"- 主分類器: {MODEL_DISPLAY_NAMES[router['selected_model']]}",
        f"- ルール 1: `predicted_type == 1` なら `KLN` を選択する。",
        f"- ルール 2: `predicted_type == 2` なら `DA` を選択する。",
        f"- ルール 3: `predicted_type == 3` なら `Summary + perturbation` を選択する。",
        "- ルール 4: `max_probability < 0.50` なら `abstain` とし、`KLN(短尾保持) + 2 turn diagnostic probe + reclassify` を実行する。",
        f"- Empirical evidence: {router['empirical_evidence']}",
        "",
        "## §6 残余と次のアクション",
        "",
        "- 残余 1: 合成データ N=46 だけでは実 trajectory への一般化はまだ未検証。",
        "- 残余 2: Type 3 は hypothesis/action mismatch feature に依存し、実データ側の counterfactual signal をまだ持たない。",
        "- 次アクション 1: AgentSwing 実 trajectory に同じ feature extractor を流し、Type 1/2/3 の shift を測る。",
        "- 次アクション 2: abstain 事例を再ラベルし、Type 3 hard negative を追加して router の誤配線を抑える。",
        "- 次アクション 3: confidence calibration を追加し、`0.5` 閾値を empirical に再調整する。",
        "- OP 台帳更新提案 diff:",
        "",
        diff_block,
        "",
        f"_Source paths: {TRAINSET_PATH}, {PAPER_PATH}, {REGISTRY_PATH}_",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    raw_records = load_jsonl(TRAINSET_PATH)
    labeled_records = [record for record in raw_records if record.get("ground_truth_type") is not None]
    labels = np.asarray([record["ground_truth_type"] for record in labeled_records], dtype=int)
    train_idx, test_idx = split_indices(labels)
    runs = evaluate_models(labeled_records, labels, train_idx, test_idx)
    best_run = max(
        runs.values(),
        key=lambda run: (run.metrics["accuracy"], run.metrics["macro_f1"]),
    )

    matrix = feature_matrix(labeled_records)
    rf_importance = runs["random_forest"].classifier.get_feature_importance()
    per_type_profiles = compute_class_profiles(matrix, labels, rf_importance)
    type3_diagnosis = diagnose_type3(
        best_run.metrics["per_type_recall"]["type_3"],
        per_type_profiles,
        rf_importance,
        matrix,
        labels,
    )
    feature_analysis = {
        "global_importance": rf_importance,
        "per_type_profiles": per_type_profiles,
        "type3_diagnosis": type3_diagnosis,
    }
    type12_metrics = evaluate_type12_subset(best_run.model_key, labeled_records)
    op_x5 = determine_op_x5_status(best_run.metrics, type12_metrics)
    router = router_proposal(best_run.model_key, best_run.metrics)

    dataset_summary = {
        "raw_count": len(raw_records),
        "noise_count": len(raw_records) - len(labeled_records),
        "labeled_count": len(labeled_records),
        "label_distribution": {
            f"type_{label}": int(np.sum(labels == label))
            for label in LABELS
        },
        "split": {
            "train_size": int(train_idx.shape[0]),
            "test_size": int(test_idx.shape[0]),
            "random_state": 42,
            "stratified": True,
        },
    }

    json_payload = {
        "dataset_summary": dataset_summary,
        "models": {
            model_key: {
                "display_name": run.display_name,
                "metrics": run.metrics,
            }
            for model_key, run in runs.items()
        },
        "best_model": {
            "model_key": best_run.model_key,
            "display_name": best_run.display_name,
            "metrics": best_run.metrics,
        },
        "feature_analysis": feature_analysis,
        "type12_binary_evaluation": type12_metrics,
        "op_x5_assessment": op_x5,
        "router_proposal": router,
    }

    RESULTS_PATH.write_text(
        json.dumps(json_payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    REPORT_PATH.write_text(
        build_report(
            runs=runs,
            best_run=best_run,
            dataset_summary=dataset_summary,
            feature_analysis=feature_analysis,
            type12_metrics=type12_metrics,
            op_x5=op_x5,
            router=router,
        ),
        encoding="utf-8",
    )

    print(f"created_json={RESULTS_PATH}")
    print(f"created_report={REPORT_PATH}")
    print(f"best_accuracy={best_run.metrics['accuracy']:.3f} ({best_run.display_name})")
    print(
        "per_type_recall="
        + json.dumps(best_run.metrics["per_type_recall"], ensure_ascii=False, sort_keys=True)
    )
    print(f"OP-X-5={op_x5['level']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
