import requests
import os

# Function to get the list of followers
def get_followers_list(github_username, headers):
    url = f'https://api.github.com/users/{github_username}/followers'
    followers_list = []
    
    while url:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            followers_list.extend(response.json())
            # Check for pagination and continue fetching
            if 'next' in response.links:
                url = response.links['next']['url']
            else:
                url = None
        else:
            print(f"Failed to fetch followers list: {response.status_code}")
            break

    return followers_list

# Function to save the followers list to a file
def save_followers_list_to_file(followers_list):
    try:
        file_path = os.path.join(os.getcwd(), "followers.txt")
        with open(file_path, "w") as file:
            if followers_list:
                file.write(f"You have {len(followers_list)} followers:\n\n")
                for user in followers_list:
                    file.write(f"{user['login']}\n")
                print(f"Followers list has been saved to '{file_path}'.")
            else:
                file.write("You have no followers or there was an error fetching the list.")
                print(f"No followers to write to '{file_path}'.")
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

    # Call the function to get the followers list
    followers_list = get_followers_list(github_username, headers)

    # Save the followers list to a file
    save_followers_list_to_file(followers_list)