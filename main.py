from user_simulation import generate_users, plot_users, summarize_users

def main():
    print("NTN Simulation --> Environment Setup\n")
    
    users = generate_users()
    summarize_users(users)
    plot_users(users)
    
    
if __name__ == "__main__":
    main()