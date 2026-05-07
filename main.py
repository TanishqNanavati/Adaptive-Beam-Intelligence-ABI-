# main.py

from user_simulation import generate_users, summarize_users
from satellite import (
    create_satellite,
    move_satellite
)
from visualization import (
    plot_users_and_satellite,
    plot_satellite_path
)
from coverage import (
    compute_coverage,
    compute_signal_strength,
    coverage_metrics
)
from optimization import compute_user_centroid
from config import BEAM_RADIUS
from comparison import plot_metric_comparison


def main():

    print("=== Adaptive Beam Intelligence ===\n")

    # -----------------------------------
    # Generate Users
    # -----------------------------------
    print(">> Generating Users")

    users = generate_users()

    summarize_users(users)

    # -----------------------------------
    # Satellite Modeling
    # -----------------------------------
    print(">> Satellite Modeling")

    satellite = create_satellite()

    path = move_satellite(satellite)

    # -----------------------------------
    # Coverage Modeling
    # -----------------------------------
    print(">> Computing Coverage")

    covered_users, distances = compute_coverage(
        users,
        satellite,
        BEAM_RADIUS
    )

    signal_strength = compute_signal_strength(
        distances
    )

    metrics = coverage_metrics(
        covered_users,
        signal_strength
    )

    # -----------------------------------
    # Print Metrics
    # -----------------------------------
    print("\n=== Coverage Metrics ===")

    print(f"Served Users      : {metrics['served_users']}")

    print(f"Coverage Percent  : {metrics['coverage_percent']:.2f}%")

    print(f"Average Signal    : {metrics['average_signal']:.6f}")

    print()
    
    # -----------------------------------
    # Optimization Phase
    # -----------------------------------
    print(">> Running Beam Optimization")

    optimized_beam = compute_user_centroid(users)

    optimized_satellite = {
        "x": optimized_beam["x"],
        "y": optimized_beam["y"],
        "height": satellite["height"]
    }

    optimized_covered_users, optimized_distances = compute_coverage(
        users,
        optimized_satellite,
        BEAM_RADIUS
    )

    optimized_signal_strength = compute_signal_strength(
        optimized_distances
    )

    optimized_metrics = coverage_metrics(
        optimized_covered_users,
        optimized_signal_strength
    )

    # -----------------------------------
    # Optimized Metrics
    # -----------------------------------
    print("\n=== Optimized Coverage Metrics ===")

    print(f"Served Users      : {optimized_metrics['served_users']}")

    print(
        f"Coverage Percent  : "
        f"{optimized_metrics['coverage_percent']:.2f}%"
    )

    print(
        f"Average Signal    : "
        f"{optimized_metrics['average_signal']:.6f}"
    )

    improvement = (
        optimized_metrics["coverage_percent"]
        - metrics["coverage_percent"]
    )

    print(f"\nCoverage Improvement : {improvement:.2f}%\n")

    # -----------------------------------
    # Visualization
    # -----------------------------------
    print(">> Generating Visualizations")

    # Baseline visualization
    plot_users_and_satellite(
        users,
        satellite,
        covered_users,
        BEAM_RADIUS,
        save_path="outputs/baseline_coverage.png"
    )

    # Optimized visualization
    plot_users_and_satellite(
        users,
        optimized_satellite,
        optimized_covered_users,
        BEAM_RADIUS,
        save_path="outputs/optimized_coverage.png"
    )

    plot_satellite_path(
        users,
        path
    )
    
    # -----------------------------------
    # Performance Comparison
    # -----------------------------------
    print(">> Generating Performance Comparison")

    plot_metric_comparison(
        metrics,
        optimized_metrics
    )


if __name__ == "__main__":
    main()