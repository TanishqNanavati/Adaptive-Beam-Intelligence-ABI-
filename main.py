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

from config import BEAM_RADIUS


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
    # Visualization
    # -----------------------------------
    print(">> Generating Visualizations")

    plot_users_and_satellite(
        users,
        satellite,
        covered_users,
        BEAM_RADIUS
    )

    plot_satellite_path(
        users,
        path
    )


if __name__ == "__main__":
    main()