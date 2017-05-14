#!/usr/bin/env python3 -tt

import requests
import io
import os
import datetime
import time
from PIL import Image
import sys

sys.path.append('[path/to/scripts-directory]')
from emailreminder import emailReminder

class RedditPost:
    def __init__(self, data):
        self.title = data['title']
        self.url = data['url']
        self.score = data['score']
    def download(self):
        pass
    def __str__(self):
        return "{} ({}): {}".format(self.title, self.score, self.url)
    def __repr__(self):
        return self.__str__()

r = requests.get('http://www.reddit.com/r/nfl.json', headers={'User-Agent': 'Reddit Script by James'})
list_of_posts = r.json()['data']['children']
reddit_posts = [RedditPost(post['data']) for post in list_of_posts]
for post in reddit_posts:
    title = post.title.lower()
    post_involves_skins = 'redskins' in title or 'washington' in title
    if post_involves_skins:
        emailReminder("{} ({})".format(post.title, post.url))
        

