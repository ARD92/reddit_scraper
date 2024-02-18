__author__ = "ARD92"

import praw
import pprint
import json
import argparse


#Login details. Reddit script app must be
#created in order to get the values for params
def login(clientid, secret, username, password, useragent):
        reddit = praw.Reddit(
                client_id=clientid,
                client_secret=secret,
                username=username,
                password = password,
                user_agent = useragent
        )
        return reddit

# Unsubscribe from all subreddits. subreddits provided as a list input
def unsubscribe(reddit, unsub):
        for i in unsub:
                try:
                        reddit.subreddit(i).unsubscribe()
                        print("unsubscribed {}".format(i))
                except prawcore.exceptions.NotFound:
                        continue


#List all subscribed subreddits
def readSubscribed(reddit):
        subr = []
        for subreddit in reddit.user.subreddits(limit=None):
                subr.append(str(subreddit))
        return subr


if __name__ == "__main__":
        #To_add: argument for login file and subreddit input
        with open('login.json', 'r') as f:
                fdata = json.load(f)

        reddit = login(fdata["client_id"], fdata["client_secret"], fdata["username"], fdata["password"], fdata["user_agent"])
        # read all subscribed subreddits
        subr = readSubscribed(reddit)
        # unsubscribe from all subreddits
        unsubscribe(reddit, subr)
