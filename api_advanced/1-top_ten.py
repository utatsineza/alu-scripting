#!/usr/bin/python3
"""
This module defines a function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API for the top 10 hot posts in a subreddit.
    If the subreddit is invalid, prints None.

    Args:
        subreddit (str): The subreddit to query.
    """
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
        else:
            print(None)
    else:
        # Invalid subreddit case
        print(None)

