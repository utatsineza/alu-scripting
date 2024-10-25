#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests

def top_ten(subreddit):
    # Define the URL and headers to avoid following redirects
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Make a GET request to Reddit's API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the subreddit is valid (status code should be 200)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        
        # If there are posts, print their titles
        if len(posts) > 0:
            for post in posts[:10]:
                print(post['data']['title'])
            print("OK")  # Explicitly printing "OK" for valid subreddits
        else:
            print("None")  # Handle case where subreddit is valid but has no posts
    else:
        # Invalid subreddit case
        print("None")

