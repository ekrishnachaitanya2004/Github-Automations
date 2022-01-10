import requests
import os

# Function to read usernames from list.txt
def read_usernames_from_file(file_name="list.txt"):
    try:
        with open(file_name, "r") as file:
            # Read all lines and remove empty lines
            usernames = [line.strip() for line in file.readlines() if line.strip()]
        return usernames
    except FileNotFoundError:
        print(f"{file_name} not found. Please make sure it exists.")
        return []

# Function to unfollow users on GitHub
def unfollow_users(github_username, github_token, users_to_unfollow):
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    for user in users_to_unfollow:
        url = f'https://api.github.com/user/following/{user}'
        response = requests.delete(url, headers=headers)
        
        if response.status_code == 204:
            print(f"Successfully unfollowed {user}.")
        else:
            print(f"Failed to unfollow {user}: {response.status_code}")

if __name__ == '__main__':
    # Print current working directory
    print("Current Directory:", os.getcwd())

    # Get GitHub username and Personal Access Token from user input
    github_username = input("Enter your GitHub username: ")
    github_token = input("Enter your GitHub Personal Access Token (PAT): ")

    # Read usernames from the list.txt file
    users_to_unfollow = read_usernames_from_file("list.txt")

    if users_to_unfollow:
        print(f"Unfollowing {len(users_to_unfollow)} users from list.txt...")
        unfollow_users(github_username, github_token, users_to_unfollow)
    else:
        print("No users to unfollow.")