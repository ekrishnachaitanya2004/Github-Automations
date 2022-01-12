import requests
import os

# Function to get the list of users you are following
def get_following_list(github_username, headers):
    url = f'https://api.github.com/users/{github_username}/following'
    following_list = []
    
    while url:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            following_list.extend(response.json())
            # Check for pagination and continue fetching
            if 'next' in response.links:
                url = response.links['next']['url']
            else:
                url = None
        else:
            print(f"Failed to fetch following list: {response.status_code}")
            break

    return following_list

# Function to save the following list to a file
def save_following_list_to_file(following_list):
    try:
        file_path = os.path.join(os.getcwd(), "list.txt")
        with open(file_path, "w") as file:
            if following_list:
                file.write(f"You are following {len(following_list)} users:\n\n")
                for user in following_list:
                    file.write(f"{user['login']}\n")
                print(f"Following list has been saved to '{file_path}'.")
            else:
                file.write("You are not following anyone or there was an error fetching the list.")
                print(f"No users to write to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

if __name__ == '__main__':
    # Print current working directory
    print("Current Directory:", os.getcwd())

    # Get GitHub username and Personal Access Token from user input
    github_username = input("Enter your GitHub username: ")
    github_token = input("Enter your GitHub Personal Access Token (PAT): ")

    # Set up the headers for API requests
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Call the function to get the following list
    following_list = get_following_list(github_username, headers)

    # Save the following list to a file
    save_following_list_to_file(following_list)