import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os
from config import (
    GRID_SIZE,
    NUM_USERS,
    RANDOM_SEED,
    ENABLE_CLUSTER,
    CLUSTER_CENTER_X,
    CLUSTER_CENTER_Y,
    CLUSTER_SPREAD,
    CLUSTER_RATIO
)

def generate_users(
    num_users=NUM_USERS,
    grid_size=GRID_SIZE,
    seed=RANDOM_SEED
):
    """
    Generate user positions.

    Supports:
    - Uniform random users
    - Clustered hotspot users

    Returns:
        np.ndarray: User positions
    """

    rng = np.random.default_rng(seed)

    # -----------------------------------
    # Uniform Distribution
    # -----------------------------------
    if not ENABLE_CLUSTER:

        users = rng.uniform(
            0,
            grid_size,
            size=(num_users, 2)
        )

        print("[✓] Generated uniformly distributed users")

        return users

    # -----------------------------------
    # Clustered Distribution
    # -----------------------------------
    cluster_users = int(num_users * CLUSTER_RATIO)

    random_users = num_users - cluster_users

    # Generate clustered users
    cluster_x = rng.normal(
        CLUSTER_CENTER_X,
        CLUSTER_SPREAD,
        cluster_users
    )

    cluster_y = rng.normal(
        CLUSTER_CENTER_Y,
        CLUSTER_SPREAD,
        cluster_users
    )

    clustered = np.column_stack((cluster_x, cluster_y))

    # Generate remaining random users
    random_part = rng.uniform(
        0,
        grid_size,
        size=(random_users, 2)
    )

    # Combine both
    users = np.vstack((clustered, random_part))

    # Keep users inside grid boundaries
    users = np.clip(users, 0, grid_size)

    print(
        f"[✓] Generated clustered users "
        f"({cluster_users} hotspot + {random_users} random)"
    )

    return users

def plot_users(users,save_path="outputs/users.png"):
    """
    Plot user distributions on 2D grid.
    
    Args:
        users (np.ndarray) : User Positions
        save_path (str) : Path to save plot
    """
    
    os.makedirs("outputs",exist_ok=True)
    
    fig,ax = plt.subplots(figsize=(8,8))
    
    ax.scatter(
        users[:,0],users[:,1],
        c='steelblue',s=20,alpha=0.7,label=f'Users (n : {len(users)})'
    )
    
    ax.set_xlim(0, GRID_SIZE)
    ax.set_ylim(0, GRID_SIZE)
    ax.set_xlabel("X Position (km)", fontsize=12)
    ax.set_ylabel("Y Position (km)", fontsize=12)
    ax.set_title("Ground User Distribution", fontsize=14, fontweight='bold')
    ax.legend(loc='upper right')
    ax.grid(True, linestyle='--', alpha=0.4)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.show()
    print(f"[✓] Plot saved to {save_path}")
    
    
def summarize_users(users):
    """
    Print statistics about user distribution.

    Args:
        users (np.ndarray): User Positions
    """
    
    print("\n--- User Distribution Summary ---")
    print(f"  Total Users   : {len(users)}")
    print(f"  X Range       : {users[:, 0].min():.2f} km  →  {users[:, 0].max():.2f} km")
    print(f"  Y Range       : {users[:, 1].min():.2f} km  →  {users[:, 1].max():.2f} km")
    print(f"  Mean Position : ({users[:, 0].mean():.2f}, {users[:, 1].mean():.2f}) km")
    print(f"  Std Dev       : ({users[:, 0].std():.2f}, {users[:, 1].std():.2f}) km")
    print("---------------------------------\n")
