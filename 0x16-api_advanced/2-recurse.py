#!/usr/bin/python3
"""
Function that queries the Reddit API
"""
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    try:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        res = get(url, headers={'User-agent': 'hAxr'}, params={'after': after},
                  allow_redirects=False).json()
        after = res['data']['after']
        for item in res['data']['children']:
            hot_list.append(item['data']['title'])
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list if len(hot_list) > 0 else None
    except:
        return None
