import requests

def get_github_repos(username, token):
    # Construct the URL for the GitHub API endpoint to list user's repositories
    url = f"https://api.github.com/users/{username}/repos"
    
    # Prepare the request headers with the access token
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"  # GitHub API version
    }
    
    try:
        # Send GET request to GitHub API
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for bad response status
        
        # Parse JSON response
        repos = response.json()
        
        # Print repository names
        for repo in repos:
            print(repo["name"])
    
    except requests.exceptions.HTTPError as err:
        print(f"Error fetching repositories: {err}")

if __name__ == "__main__":
    # GitHub username and personal access token (replace with your own)
    username = "your_github_username"
    token = "your_personal_access_token"
    
    # Call function to get repositories
    get_github_repos(username, token)
