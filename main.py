# main.py
from user_simulation import generate_users, summarize_users
from satellite import create_satellite, move_satellite
from visualization import plot_users_and_satellite, plot_satellite_path

def main():
    print("=== NTN Signal Optimization Simulation ===\n")

    # Phase 1 - Users
    print(">> Phase 1: Generating Users")
    users = generate_users()
    summarize_users(users)

    # Phase 2 - Satellite
    print(">> Phase 2: Satellite Modeling")
    satellite = create_satellite()
    path = move_satellite(satellite)

    # Visualize
    plot_users_and_satellite(users, satellite)
    plot_satellite_path(users, path)

if __name__ == "__main__":
    main()