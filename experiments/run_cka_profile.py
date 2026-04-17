#!/usr/bin/env python3
"""CKA 忘却場プロファイル — Paper III 定理 4.5.1 間接検証
/exe 全指摘修正版 (v2.1)

修正:
  C-1: 合成テンプレート → WikiText-103 実データ
  W-1: binom_test → binomtest
  W-2: N<d 時の CKA 数値安定性 → Gram 行列版
  W-3: パディングトークン混入 → attention_mask 対応
  W-4: GPT-2 12層 → Mistral-7B-v0.1 32層 (Colab L4 対応)
  W-5: 反転点検出 → 平滑化 + 閾値ベース
  I-1〜3: legend重複, device指定, seed設定
"""

import torch
import numpy as np
import matplotlib.pyplot as plt
import json
import sys
from pathlib import Path

# 再現性
SEED = 42
np.random.seed(SEED)
torch.manual_seed(SEED)


# === CKA 計算 (Gram 行列版: N < d に安定) ===

def linear_cka_gram(X: np.ndarray, Y: np.ndarray) -> float:
    """線形 CKA (Kornblith et al. 2019) — Gram 行列版
    X, Y: (N, d) — 中心化済み表現行列
    N < d のとき X.T @ X (d×d) より X @ X.T (N×N) が数値的に安定
    """
    N = X.shape[0]
    # Gram 行列 (N×N)
    GX = X @ X.T  # (N, N)
    GY = Y @ Y.T  # (N, N)

    # HSIC (線形カーネル) の Gram 行列版
    hsic_xy = np.sum(GX * GY)           # tr(GX @ GY) = Frobenius内積
    hsic_xx = np.sum(GX * GX)           # tr(GX @ GX)
    hsic_yy = np.sum(GY * GY)           # tr(GY @ GY)

    denom = np.sqrt(hsic_xx) * np.sqrt(hsic_yy)
    if denom < 1e-12:
        return 0.0
    return float(hsic_xy / denom)


# === Hidden state 抽出 ===

def extract_hidden_states(
    model_name: str,
    n_samples: int = 500,
    max_length: int = 64,
    batch_size: int = 8,
    device: str = "auto",
) -> list[np.ndarray]:
    """各層の hidden state を抽出 (実データ使用)

    Returns:
        hidden_states: [(N, d)] × (L+1) — 各層の表現行列
    """
    from transformers import AutoModelForCausalLM, AutoTokenizer

    # デバイス選択
    if device == "auto":
        device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"  デバイス: {device}")

    # モデル読込 (float16 for GPU メモリ節約)
    dtype = torch.float16 if device == "cuda" else torch.float32
    print(f"  モデル読込中: {model_name} (dtype={dtype})...")
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=dtype,
        device_map=device if device == "cuda" else None,
        low_cpu_mem_usage=True,
    )
    if device != "cuda":
        model = model.to(device)
    model.eval()

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # 実データ取得 (WikiText-103)
    print(f"  データ取得中 (WikiText-103, N={n_samples})...")
    try:
        from datasets import load_dataset
        ds = load_dataset("wikitext", "wikitext-103-raw-v1", split="test")
        # 空行・短文を除外し十分な長さのテキストを収集
        texts = []
        for row in ds:
            t = row["text"].strip()
            if len(t) > 80:  # 十分な長さ
                texts.append(t)
            if len(texts) >= n_samples:
                break
        if len(texts) < n_samples:
            print(f"  ⚠️ {n_samples} サンプル要求に対し {len(texts)} しか取得できず")
            n_samples = len(texts)
    except Exception as e:
        print(f"  ⚠️ datasets ライブラリ不可 ({e}), フォールバック: 多様な合成テキスト")
        # フォールバック: テンプレート単一文の代わりに多様なシード文を生成
        import hashlib
        templates = [
            "The fundamental principles of {} involve understanding how",
            "In the context of modern {}, researchers have discovered that",
            "A comprehensive analysis of {} reveals important connections between",
            "The mathematical foundations of {} rest upon several key axioms",
            "Recent developments in {} suggest a paradigm shift toward",
        ]
        topics = [
            "quantum mechanics", "information theory", "neural networks",
            "statistical mechanics", "category theory", "differential geometry",
            "topology", "number theory", "algebraic structures", "machine learning",
            "cognitive science", "thermodynamics", "optimization", "probability",
            "dynamical systems", "signal processing", "graph theory", "logic",
            "automata theory", "control theory",
        ]
        texts = []
        for i in range(n_samples):
            t = templates[i % len(templates)].format(topics[i % len(topics)])
            h = hashlib.md5(str(i).encode()).hexdigest()[:16]
            texts.append(f"{t} {h} in the year {2000 + i % 26}")

    print(f"  テキスト数: {len(texts)}")

    # バッチ処理で hidden states 抽出
    all_hidden = []  # [layer_idx] -> list of (batch_valid, d)
    n_collected = 0

    for batch_start in range(0, len(texts), batch_size):
        batch_texts = texts[batch_start:batch_start + batch_size]
        inputs = tokenizer(
            batch_texts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=max_length,
        ).to(device if device != "cuda" else model.device)

        with torch.no_grad():
            outputs = model(**inputs, output_hidden_states=True)

        attention_mask = inputs["attention_mask"]  # (B, T)

        for layer_idx, h in enumerate(outputs.hidden_states):
            if len(all_hidden) <= layer_idx:
                all_hidden.append([])

            # W-3 修正: 各サンプルの最終非パディングトークンを取得
            # attention_mask の最後の 1 の位置
            for b in range(h.shape[0]):
                # 各サンプルのマスクから最終有効位置を取得
                mask_b = attention_mask[b]  # (T,)
                last_valid = mask_b.sum().item() - 1  # 最後の 1 の位置
                token_repr = h[b, last_valid, :].float().cpu().numpy()
                all_hidden[layer_idx].append(token_repr)

        n_collected += len(batch_texts)
        if n_collected % 100 == 0 or n_collected >= len(texts):
            print(f"  ... {n_collected}/{len(texts)} サンプル処理")

    # 結合: [(N, d)] × (L+1)
    hidden_states = [np.stack(layer_reprs, axis=0) for layer_reprs in all_hidden]
    print(f"  層数: {len(hidden_states)} (embedding {hidden_states[0].shape} 含む)")

    # メモリ解放
    del model
    if device == "cuda":
        torch.cuda.empty_cache()

    return hidden_states


# === CKA プロファイル計算 ===

def compute_cka_profile(hidden_states: list[np.ndarray]) -> dict:
    """CKA 忘却場プロファイルの計算"""
    # 中心化
    hidden_centered = [h - h.mean(axis=0) for h in hidden_states]

    h0 = hidden_centered[0]  # 入力層 (embedding)
    N, d = h0.shape
    L = len(hidden_centered)

    print(f"  CKA 計算中 (N={N}, d={d}, L={L})...")
    print(f"  CKA モード: {'Gram行列版 (N<d)' if N < d else '標準版 (N≥d)'}")

    # Φ(l) = 1 - CKA(h_l, h_0)
    phi = []
    for l in range(L):
        cka_val = linear_cka_gram(hidden_centered[l], h0)
        phi.append(1.0 - cka_val)
    phi = np.array(phi)

    # 二階差分 (曲率プロキシ)
    k_hat_raw = np.diff(phi, n=2)

    # W-5 修正: 平滑化 (window=3 の移動平均) で反転点のノイズ除去
    if len(k_hat_raw) >= 5:
        window = 3
        kernel = np.ones(window) / window
        k_hat_smooth = np.convolve(k_hat_raw, kernel, mode="same")
    else:
        k_hat_smooth = k_hat_raw

    # 反転点検出: 平滑化後の符号変化 + 閾値 (ノイズ区間除外)
    threshold = np.std(k_hat_smooth) * 0.1  # ノイズフロア
    k_sign = np.zeros_like(k_hat_smooth)
    k_sign[k_hat_smooth > threshold] = 1
    k_sign[k_hat_smooth < -threshold] = -1
    # k_sign == 0 (閾値内) は前の符号を引き継ぐ
    for i in range(1, len(k_sign)):
        if k_sign[i] == 0:
            k_sign[i] = k_sign[i - 1]

    sign_changes = np.where(np.diff(k_sign) != 0)[0]

    return {
        "n_layers": L,
        "n_samples": hidden_states[0].shape[0],
        "dim": hidden_states[0].shape[1],
        "phi": phi,
        "k_hat_raw": k_hat_raw,
        "k_hat_smooth": k_hat_smooth,
        "sign_changes": sign_changes,
        "threshold": threshold,
    }


# === 可視化 ===

def plot_results(results: dict, model_name: str, save_path: str = None):
    """結果の可視化"""
    fig, axes = plt.subplots(3, 1, figsize=(12, 12), sharex=False)

    L = results["n_layers"]
    N = results["n_samples"]
    d = results["dim"]

    # (a) Φ_CKA プロファイル
    ax1 = axes[0]
    layers = np.arange(L)
    ax1.plot(layers, results["phi"], "b-o", markersize=3, linewidth=1.5,
             label=r"$\Phi_{\mathrm{CKA}}(l) = 1 - \mathrm{CKA}(h_l, h_0)$")
    ax1.set_ylabel(r"$\Phi_{\mathrm{CKA}}(l)$", fontsize=12)
    ax1.set_xlabel("層 l", fontsize=12)
    ax1.set_title(f"{model_name} — CKA 忘却場プロファイル (N={N}, d={d})", fontsize=13)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)

    # (b) 二階差分 (raw + smooth)
    ax2 = axes[1]
    k_layers = np.arange(1, L - 1)
    ax2.bar(k_layers, results["k_hat_raw"], alpha=0.3, color="gray", label="raw")
    ax2.plot(k_layers, results["k_hat_smooth"], "k-o", markersize=3, linewidth=1.5,
             label="smoothed (window=3)")
    ax2.axhline(y=0, color="black", linestyle="-", linewidth=0.5)
    ax2.axhline(y=results["threshold"], color="orange", linestyle="--", alpha=0.5,
                label=f"threshold (±{results['threshold']:.4f})")
    ax2.axhline(y=-results["threshold"], color="orange", linestyle="--", alpha=0.5)
    ax2.set_ylabel(r"$\hat{K}(l)$", fontsize=12)
    ax2.set_xlabel("層 l", fontsize=12)
    ax2.set_title(r"曲率プロキシ $\hat{K}(l)$: 二階差分", fontsize=13)

    # 反転点マーク (重複ラベル修正)
    for i, sc in enumerate(results["sign_changes"]):
        label = f"反転点 l*={sc + 1}" if i == 0 else None
        ax2.axvline(x=sc + 1, color="green", linestyle="--", alpha=0.7, label=label)
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)

    # (c) 累積符号比率 (前半 vs 後半)
    ax3 = axes[2]
    k_smooth = results["k_hat_smooth"]
    cum_pos = np.cumsum(k_smooth > results["threshold"])
    cum_neg = np.cumsum(k_smooth < -results["threshold"])
    ax3.plot(k_layers, cum_pos, "b-", linewidth=2, label=r"累積 $\hat{K} > 0$ (凸, K>0相当)")
    ax3.plot(k_layers, cum_neg, "r-", linewidth=2, label=r"累積 $\hat{K} < 0$ (凹, K≤0相当)")
    mid_layer = k_layers[len(k_layers) // 2]
    ax3.axvline(x=mid_layer, color="gray", linestyle=":", alpha=0.5, label=f"中間点 l={mid_layer}")
    ax3.set_ylabel("累積カウント", fontsize=12)
    ax3.set_xlabel("層 l", fontsize=12)
    ax3.set_title("符号累積分布 (P-1/P-2 検証)", fontsize=13)
    ax3.legend(fontsize=9)
    ax3.grid(True, alpha=0.3)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches="tight")
        print(f"  図を保存: {save_path}")
    plt.show()


# === 統計検定 ===

def statistical_test(results: dict) -> dict:
    """統計検定: 二階差分の符号分布"""
    from scipy import stats

    k_hat = results["k_hat_smooth"]
    threshold = results["threshold"]

    # 閾値を超える有意な符号のみカウント
    n_pos = int(np.sum(k_hat > threshold))
    n_neg = int(np.sum(k_hat < -threshold))
    n_neutral = int(np.sum(np.abs(k_hat) <= threshold))
    n_total = n_pos + n_neg  # 中立を除外

    # W-1 修正: binomtest (scipy ≥ 1.7)
    if n_total > 0:
        binom_result = stats.binomtest(n_pos, n_total, 0.5, alternative="two-sided")
        binom_p = binom_result.pvalue
    else:
        binom_p = 1.0

    # 前半 vs 後半の符号比較
    mid = len(k_hat) // 2
    first_half = k_hat[:mid]
    second_half = k_hat[mid:]

    first_pos_rate = float(np.mean(first_half > threshold)) if len(first_half) > 0 else 0
    second_pos_rate = float(np.mean(second_half > threshold)) if len(second_half) > 0 else 0
    first_neg_rate = float(np.mean(first_half < -threshold)) if len(first_half) > 0 else 0
    second_neg_rate = float(np.mean(second_half < -threshold)) if len(second_half) > 0 else 0

    # Mann-Whitney U: 前半 vs 後半の分布差
    if len(first_half) > 1 and len(second_half) > 1:
        mw_stat, mw_p = stats.mannwhitneyu(first_half, second_half, alternative="two-sided")
    else:
        mw_stat, mw_p = 0, 1.0

    return {
        "n_positive": n_pos,
        "n_negative": n_neg,
        "n_neutral": n_neutral,
        "binom_p": float(binom_p),
        "mann_whitney_U": float(mw_stat),
        "mann_whitney_p": float(mw_p),
        "first_half_pos_rate": first_pos_rate,
        "second_half_pos_rate": second_pos_rate,
        "first_half_neg_rate": first_neg_rate,
        "second_half_neg_rate": second_neg_rate,
        "sign_changes": results["sign_changes"].tolist(),
        "n_sign_changes": len(results["sign_changes"]),
        # 予測判定
        "P1_shallow_convex": first_pos_rate > first_neg_rate,    # 浅層で凸優位
        "P2_deep_concave": second_neg_rate > second_pos_rate,    # 深層で凹優位
        "P3_inversion_exists": len(results["sign_changes"]) > 0, # 反転点あり
    }


# === メイン ===

def main():
    import argparse
    parser = argparse.ArgumentParser(description="CKA 忘却場プロファイル — Paper III 定理 4.5.1 間接検証")
    parser.add_argument("--model", default="mistralai/Mistral-7B-v0.1",
                        help="モデル名 (default: Mistral-7B-v0.1, 32層)")
    parser.add_argument("--n_samples", type=int, default=500,
                        help="サンプル数 (default: 500)")
    parser.add_argument("--batch_size", type=int, default=4,
                        help="バッチサイズ (default: 4, VRAM節約)")
    parser.add_argument("--max_length", type=int, default=64,
                        help="最大トークン長 (default: 64)")
    parser.add_argument("--device", default="auto",
                        help="デバイス (auto/cuda/cpu)")
    parser.add_argument("--save_dir", default=".",
                        help="結果保存ディレクトリ")
    args = parser.parse_args()

    print("=" * 60)
    print("CKA 忘却場プロファイル — Paper III 定理 4.5.1 間接検証")
    print(f"モデル: {args.model}")
    print(f"サンプル数: {args.n_samples}, バッチ: {args.batch_size}")
    print("=" * 60)

    # Phase 1: Hidden state 抽出
    print("\n[Phase 1] Hidden state 抽出")
    hidden_states = extract_hidden_states(
        model_name=args.model,
        n_samples=args.n_samples,
        max_length=args.max_length,
        batch_size=args.batch_size,
        device=args.device,
    )

    # Phase 2: CKA プロファイル計算
    print("\n[Phase 2] CKA プロファイル計算")
    results = compute_cka_profile(hidden_states)

    # Phase 3: 統計検定
    print("\n[Phase 3] 統計検定")
    test_results = statistical_test(results)

    print("\n--- 統計検定結果 ---")
    for k, v in test_results.items():
        print(f"  {k}: {v}")

    # Phase 4: 可視化
    print("\n[Phase 4] 可視化")
    save_dir = Path(args.save_dir)
    save_dir.mkdir(parents=True, exist_ok=True)
    model_short = args.model.split("/")[-1]
    fig_path = str(save_dir / f"cka_profile_{model_short}.png")
    plot_results(results, args.model, save_path=fig_path)

    # Phase 5: 反証条件チェック
    print("\n=== 反証条件チェック (D-02) ===")
    if not test_results["P3_inversion_exists"]:
        print("  ⚠️ F-1: 反転点なし → H₁ 棄却")
        verdict = "REFUTED_F1"
    elif not test_results["P1_shallow_convex"]:
        print("  ⚠️ F-2 兆候: 浅層で凸が支配的でない")
        verdict = "SUSPECT_F2"
    elif not test_results["P2_deep_concave"]:
        print("  ⚠️ F-2 兆候: 深層で凹が支配的でない")
        verdict = "SUSPECT_F2"
    else:
        print("  ✅ H₁ 暫定的に維持")
        verdict = "SUPPORTED"

    # JSON出力
    output = {
        "model": args.model,
        "n_samples": args.n_samples,
        "n_layers": results["n_layers"],
        "dim": results["dim"],
        "phi": results["phi"].tolist(),
        "k_hat_raw": results["k_hat_raw"].tolist(),
        "k_hat_smooth": results["k_hat_smooth"].tolist(),
        "sign_changes": results["sign_changes"].tolist(),
        "test_results": test_results,
        "verdict": verdict,
    }
    json_path = save_dir / f"cka_results_{model_short}.json"
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\n  結果を保存: {json_path}")


if __name__ == "__main__":
    main()
