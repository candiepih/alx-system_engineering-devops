#!/usr/bin/python3
""" Function that queries the Reddit API and
returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ Queries Reddit API
    Args:
        subreddit (string): Name of subreddit to query
    Returns:
        Number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url, headers={'User-Agent': 'Python/requests'})
    try:
        response = r.json()
        return response.get("data", {}).get("subscribers", 0)
    except Exception:
        return 0
