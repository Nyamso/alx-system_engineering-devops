#!/usr/bin/python3
"""Function to query subscribers"""
import requests

def number_of_subscribers(subreddit):
"""Return the total number of subscribers"""
	url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
	headers =  requests.utils.default_headers()
	headers.update({'User-Agent': 'My User Agent 1.0'})

	r = requests.get(url, headers=headers).json()
	subscribers = r.get('data', {}).get('subscribers')
	if not subscribers:
		return 0
	return subscribers
