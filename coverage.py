# coverage.py
# Baseline satellite beam coverage model

import numpy as np


def compute_coverage(users, satellite, beam_radius):
    """
    Determine which users are covered by the satellite beam.

    Args:
        users (np.ndarray): User positions
        satellite (dict): Satellite state
        beam_radius (float): Coverage radius in km

    Returns:
        covered_users (np.ndarray): Boolean mask
        distances (np.ndarray): Distance of each user from satellite
    """

    sat_x = satellite["x"]
    sat_y = satellite["y"]

    # Compute 2D Euclidean distance
    distances = np.sqrt(
        (users[:, 0] - sat_x) ** 2 +
        (users[:, 1] - sat_y) ** 2
    )

    # Users inside beam radius
    covered_users = distances <= beam_radius

    return covered_users, distances



def compute_signal_strength(distances):
    """
    Compute signal strength using inverse square law.

    Args:
        distances (np.ndarray): User distances

    Returns:
        np.ndarray: Signal strengths
    """

    epsilon = 1e-6  # avoid division by zero

    signal_strength = 1 / ((distances + epsilon) ** 2)

    return signal_strength



def coverage_metrics(covered_users, signal_strength):
    """
    Compute baseline coverage metrics.

    Args:
        covered_users (np.ndarray): Boolean mask
        signal_strength (np.ndarray): Signal strengths

    Returns:
        dict: Metrics
    """

    total_users = len(covered_users)
    served_users = np.sum(covered_users)

    coverage_percent = (served_users / total_users) * 100

    avg_signal = np.mean(signal_strength[covered_users])

    metrics = {
        "served_users": served_users,
        "coverage_percent": coverage_percent,
        "average_signal": avg_signal
    }

    return metrics