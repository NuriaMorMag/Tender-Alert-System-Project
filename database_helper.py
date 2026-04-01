# File used as a simple database
DB_FILE = "users.json"

def save_user(email, description):
    # Initialize empty list
    users = []

    # If file exists, load existing users
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            users = json.load(f)

    # Add new user
    users.append({
        "email": email,
        "description": description,
        "verified": False  # user is not verified yet
    })

    # Save updated list back to file
    with open(DB_FILE, "w") as f:
        json.dump(users, f, indent=4)