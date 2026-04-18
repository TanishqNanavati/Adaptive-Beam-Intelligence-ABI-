import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os
from config import GRID_SIZE, NUM_USERS, RANDOM_SEED

def generate_users(num_users=NUM_USERS,grid_size=GRID_SIZE,seed=RANDOM_SEED):
    """
    Generate random user positions within the grid.
    
    Returns:
        users (np.ndarray) : Array of users of shape
                            (num_users,2) where each 
                            row is (x,y)
    """
    
    rng = np.random.default_rng(seed)
    users = rng.uniform(0,grid_size,size=(num_users,2))
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
