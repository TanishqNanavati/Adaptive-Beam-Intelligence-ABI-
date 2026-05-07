# optimization.py
# Adaptive beam optimization logic

import numpy as np


def compute_user_centroid(users):
    """
    Compute centroid (average position) of all users.

    Args:
        users (np.ndarray): User positions

    Returns:
        dict: Optimized beam center
    """

    centroid_x = np.mean(users[:, 0])

    centroid_y = np.mean(users[:, 1])

    optimized_beam = {
        "x": centroid_x,
        "y": centroid_y
    }

    print(
        f"[✓] Optimized beam center computed at "
        f"({centroid_x:.2f}, {centroid_y:.2f})"
    )

    return optimized_beam