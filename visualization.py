# visualization.py
# Centralized visualization functions

import matplotlib.pyplot as plt
import os
from config import GRID_SIZE


def plot_users_and_satellite(users, satellite, save_path="outputs/satellite.png"):
    """
    Plot users and satellite position on the 2D grid.

    Args:
        users (np.ndarray): User positions (N, 2)
        satellite (dict): Satellite state
        save_path (str): Output path for plot
    """
    os.makedirs("outputs", exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot users
    ax.scatter(
        users[:, 0], users[:, 1],
        c='steelblue', s=20, alpha=0.7, label=f'Users (n={len(users)})'
    )

    # Plot satellite
    ax.scatter(
        satellite["x"], satellite["y"],
        c='red', s=200, marker='*', zorder=5,
        label=f'Satellite (alt={satellite["height"]} km)'
    )

    ax.set_xlim(0, GRID_SIZE)
    ax.set_ylim(0, GRID_SIZE)
    ax.set_xlabel("X Position (km)", fontsize=12)
    ax.set_ylabel("Y Position (km)", fontsize=12)
    ax.set_title("Satellite Position over User Grid", fontsize=14, fontweight='bold')
    ax.legend(loc='upper right')
    ax.grid(True, linestyle='--', alpha=0.4)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    print(f"[✓] Plot saved to {save_path}")


def plot_satellite_path(users, path, save_path="outputs/path.png"):
    """
    Plot satellite movement path over the user grid.

    Args:
        users (np.ndarray): User positions
        path (list of tuples): Satellite (x, y) positions over time
        save_path (str): Output path
    """
    os.makedirs("outputs", exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot users
    ax.scatter(
        users[:, 0], users[:, 1],
        c='steelblue', s=20, alpha=0.5, label=f'Users (n={len(users)})'
    )

    # Plot path
    path_x = [p[0] for p in path]
    path_y = [p[1] for p in path]

    ax.plot(path_x, path_y, 'r--', linewidth=1.5, alpha=0.7, label='Satellite Path')
    ax.scatter(path_x, path_y, c='red', s=60, zorder=5)

    # Mark start and end
    ax.scatter(path_x[0], path_y[0], c='green', s=150, marker='^', zorder=6, label='Start')
    ax.scatter(path_x[-1], path_y[-1], c='black', s=150, marker='s', zorder=6, label='End')

    ax.set_xlim(0, GRID_SIZE)
    ax.set_ylim(0, GRID_SIZE)
    ax.set_xlabel("X Position (km)", fontsize=12)
    ax.set_ylabel("Y Position (km)", fontsize=12)
    ax.set_title("Satellite Movement Path", fontsize=14, fontweight='bold')
    ax.legend(loc='upper right')
    ax.grid(True, linestyle='--', alpha=0.4)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    print(f"[✓] Plot saved to {save_path}")