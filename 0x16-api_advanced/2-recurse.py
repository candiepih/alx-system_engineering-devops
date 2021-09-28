#!/usr/bin/python3
""" Function that queries the Reddit API and
prints the titles of all hot posts using recursion
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Queries recursively the Reddit API
    Args:
        subreddit (string): Name of subreddit to query
        hot_list (list): list of titles of hot posts
        after (string): id of the next subreddit page
    Returns:
        list of subreddit hot posts or None if subreddit doesn't exist
    """
    params = {
        "after": after
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(url, headers={'User-Agent': 'Python/requests'},
                     params=params)
    try:
        response = r.json()
        posts = response.get("data", {}).get("children", None)
        after = response.get("data", {}).get("after", None)
        if posts is not None:
            [hot_list.append(p.get("data").get("title")) for p in posts]

        if after is None:
            if len(hot_list) == 0:
                return None
            return hot_list
        else:
            return recurse(subreddit, hot_list, after=after)
    except Exception:
        return None
