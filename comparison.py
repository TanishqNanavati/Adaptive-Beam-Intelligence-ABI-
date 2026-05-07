# comparison.py
# Performance comparison visualization

import matplotlib.pyplot as plt
import numpy as np
import os


def plot_metric_comparison(
    baseline_metrics,
    optimized_metrics,
    save_path="outputs/comparison.png"
):
    """
    Compare baseline vs optimized metrics using bar charts.

    Args:
        baseline_metrics (dict): Baseline system metrics
        optimized_metrics (dict): Optimized system metrics
        save_path (str): Output path
    """

    os.makedirs("outputs", exist_ok=True)

    # -----------------------------------
    # Metrics
    # -----------------------------------
    labels = [
        "Coverage %",
        "Served Users",
        "Average Signal"
    ]

    baseline_values = [
        baseline_metrics["coverage_percent"],
        baseline_metrics["served_users"],
        baseline_metrics["average_signal"]
    ]

    optimized_values = [
        optimized_metrics["coverage_percent"],
        optimized_metrics["served_users"],
        optimized_metrics["average_signal"]
    ]

    # -----------------------------------
    # Plot Setup
    # -----------------------------------
    x = np.arange(len(labels))

    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))

    # -----------------------------------
    # Baseline Bars
    # -----------------------------------
    ax.bar(
        x - width / 2,
        baseline_values,
        width,
        label="Baseline",
        alpha=0.8
    )

    # -----------------------------------
    # Optimized Bars
    # -----------------------------------
    ax.bar(
        x + width / 2,
        optimized_values,
        width,
        label="Optimized",
        alpha=0.8
    )

    # -----------------------------------
    # Formatting
    # -----------------------------------
    ax.set_xticks(x)

    ax.set_xticklabels(labels)

    ax.set_ylabel("Metric Value")

    ax.set_title(
        "Baseline vs Optimized Coverage Performance",
        fontsize=14,
        fontweight='bold'
    )

    ax.legend()

    ax.grid(True, linestyle='--', alpha=0.3)

    plt.tight_layout()

    plt.savefig(save_path, dpi=150)

    print(f"[✓] Comparison chart saved to {save_path}")