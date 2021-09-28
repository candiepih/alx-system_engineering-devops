# API advanced

Topic's aim was to understand the following concepts:-

* How to read API documentation to find the endpoints you’re looking for
* How to use an API with pagination
* How to parse JSON results from an API
* How to make a recursive API call
* How to sort a dictionary by value

# Files

The following task files were used to test understanding on the concepts

[0-subs.py](../0-subs.py)

Function that queries the [Reddit API](https://www.reddit.com/dev/api/) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return `0`.

Requirements:

* Prototype: `def number_of_subscribers(subreddit)`
* If not a valid subreddit, return `0`.
* NOTE: Invalid subreddits may return a redirect to search results. Ensure that no following redirects.

[1-top_ten.py](./1-top_ten.py)

Function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

Requirements:

* Prototype: `def top_ten(subreddit)`
* If not a valid subreddit, print `None`.
* NOTE: Invalid subreddits may return a redirect to search results. Ensure no following redirects.

[2-recurse.py](./2-recurse.py)

*Recursive function* that queries the [Reddit API](https://www.reddit.com/dev/api/) and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function returns `None`.

Requirements:

* Prototype: `def recurse(subreddit, hot_list=[])`
* Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.
* If not a valid subreddit, return `None`.
* NOTE: Invalid subreddits may return a redirect to search results. Ensure no following redirects.
