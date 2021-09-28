#!/usr/bin/python3
""" Function that queries the Reddit API and
prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """ Queries Reddit API and prints first 10 hot posts
    Args:
        subreddit (string): Name of subreddit to query
    Returns:
        Nothing
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {
        "limit": 10
    }
    r = requests.get(url, headers={'User-Agent': 'Python/requests'},
                     params=params)
    try:
        response = r.json()
        posts = response.get("data", {}).get("children", None)
        if posts is None:
            print(None)
        else:
            [print(p.get("data").get("title")) for p in posts]
    except Exception:
        print(None)
