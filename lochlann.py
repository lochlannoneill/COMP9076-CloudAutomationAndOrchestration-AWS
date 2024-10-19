import os
from reading_from_user import read_nonempty_string
from reading_from_user import read_range_integer

FILE_PASSWORDS = "passwords.txt"

# Load existing users from passwords file
def load_users():
    users = {}
    if os.path.exists(FILE_PASSWORDS):
        with open(FILE_PASSWORDS, "r") as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line:  # Only process non-empty lines
                    parts = stripped_line.split()  # Split by whitespace
                    if len(parts) == 4:  # Ensure there are exactly 4 parts
                        username, password, access_key, secret_key = parts
                        users[username] = {
                            "password": password,
                            "access_key": access_key,
                            "secret_key": secret_key
                        }
                    else:
                        print(f"Skipping line due to incorrect format: {stripped_line}")
    return users

# Authenticate existing user
def login_user(users):
    while True:
        username = read_nonempty_string("Username: ")
        password = read_nonempty_string("Password: ")
        
        # Validate credentials
        if username in users and users[username]["password"] == password:
            print(f"Welcome, {username}!")
            return users[username]
        else:
            print("Invalid username or password. Please try again.")

# Register new user
def register_user():
    username = read_nonempty_string("Enter a new username: ")
    password = read_nonempty_string("Enter a password: ")
    access_key = read_nonempty_string("Enter your AWS Access Key ID: ")
    secret_key = read_nonempty_string("Enter your AWS Secret Access Key: ")
    
    # Append new user to file
    with open(FILE_PASSWORDS, "a") as file:
        file.write(f"\n{username}\t{password}\t{access_key}\t{secret_key}")
    
    print(f"User '{username}' registered successfully.")

# Display menu options and get user's option
def display_menu():
    MENU_OPTIONS = {
        "Login": 1,
        "Register": 2
    }
    
    # Print menu options
    for option, number in MENU_OPTIONS.items():
        print(f"{number}. {option}")
    
    # Get menu option
    option = read_range_integer("Select valid option: ", min(MENU_OPTIONS.values()), max(MENU_OPTIONS.values()))
    return option

# Handle menu
def handle_menu(option, users):
    if option == 1:  # Login
        user_credentials = login_user(users)
        if user_credentials:
            return user_credentials
    elif option == 2:  # Register
        register_user()
    else:
        print("Invalid menu option.")
        
def main():
    users = load_users()
    
    while True:
        option = display_menu()
        handle_menu(option, users)

if __name__ == "__main__":
    main()