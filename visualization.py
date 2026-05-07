# visualization.py
# Centralized visualization functions

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

from config import GRID_SIZE


def plot_users_and_satellite(
    users,
    satellite,
    covered_users,
    beam_radius,
    save_path="outputs/satellite.png"
):
    """
    Plot users, satellite, and beam coverage.

    Args:
        users (np.ndarray): User positions
        satellite (dict): Satellite state
        covered_users (np.ndarray): Boolean mask for covered users
        beam_radius (float): Beam radius in km
        save_path (str): Output path
    """

    os.makedirs("outputs", exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 8))

    # ----------------------------
    # Plot Covered Users
    # ----------------------------
    ax.scatter(
        users[covered_users, 0],
        users[covered_users, 1],
        c='green',
        s=25,
        alpha=0.8,
        label='Covered Users'
    )

    # ----------------------------
    # Plot Uncovered Users
    # ----------------------------
    ax.scatter(
        users[~covered_users, 0],
        users[~covered_users, 1],
        c='gray',
        s=20,
        alpha=0.5,
        label='Uncovered Users'
    )

    # ----------------------------
    # Plot Satellite
    # ----------------------------
    ax.scatter(
        satellite["x"],
        satellite["y"],
        c='red',
        s=250,
        marker='*',
        zorder=5,
        label=f'Satellite ({satellite["height"]} km)'
    )

    # ----------------------------
    # Plot Beam Coverage Circle
    # ----------------------------
    beam = patches.Circle(
        (satellite["x"], satellite["y"]),
        radius=beam_radius,
        edgecolor='red',
        facecolor='red',
        alpha=0.15,
        linewidth=2,
        label='Beam Coverage'
    )

    ax.add_patch(beam)

    # ----------------------------
    # Formatting
    # ----------------------------
    ax.set_xlim(0, GRID_SIZE)
    ax.set_ylim(0, GRID_SIZE)

    ax.set_xlabel("X Position (km)", fontsize=12)
    ax.set_ylabel("Y Position (km)", fontsize=12)

    ax.set_title(
        "Satellite Beam Coverage",
        fontsize=14,
        fontweight='bold'
    )

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
        path (list): Satellite positions
        save_path (str): Output path
    """

    os.makedirs("outputs", exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot users
    ax.scatter(
        users[:, 0],
        users[:, 1],
        c='steelblue',
        s=20,
        alpha=0.5,
        label=f'Users (n={len(users)})'
    )

    # Extract path coordinates
    path_x = [p[0] for p in path]
    path_y = [p[1] for p in path]

    # Plot path line
    ax.plot(
        path_x,
        path_y,
        'r--',
        linewidth=1.5,
        alpha=0.7,
        label='Satellite Path'
    )

    # Plot path points
    ax.scatter(
        path_x,
        path_y,
        c='red',
        s=60,
        zorder=5
    )

    # Start marker
    ax.scatter(
        path_x[0],
        path_y[0],
        c='green',
        s=150,
        marker='^',
        zorder=6,
        label='Start'
    )

    # End marker
    ax.scatter(
        path_x[-1],
        path_y[-1],
        c='black',
        s=150,
        marker='s',
        zorder=6,
        label='End'
    )

    ax.set_xlim(0, GRID_SIZE)
    ax.set_ylim(0, GRID_SIZE)

    ax.set_xlabel("X Position (km)", fontsize=12)
    ax.set_ylabel("Y Position (km)", fontsize=12)

    ax.set_title(
        "Satellite Movement Path",
        fontsize=14,
        fontweight='bold'
    )

    ax.legend(loc='upper right')

    ax.grid(True, linestyle='--', alpha=0.4)

    plt.tight_layout()

    plt.savefig(save_path, dpi=150)

    print(f"[✓] Plot saved to {save_path}")