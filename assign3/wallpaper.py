#!/usr/local/bin/python3 -tt

import requests
import io
import os
import datetime
import time
from PIL import Image
from appscript import app, mactypes
import imagehash
import random
import simplejson

'''
A script to randomly download a wallpaper from Reddit
and set it as the desktop background. I have a cronjob
that runs this every hour.
'''

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

timestamp = time.time()
potential_queries = ['wallpapers', 'wallpaper',
                     'MinimalWallpaper', 'HI_Res']
query = potential_queries[random.randint(0, len(potential_queries) - 1)]
r = requests.get('http://www.reddit.com/r/{}.json'.format(query),
                 headers={'User-Agent': 'Wallscraper Script by James'})
if r.status_code != 200:
    raise RuntimeError("Reddit didn't load")

list_of_posts = r.json()['data']['children']
reddit_posts = [RedditPost(post['data']) for post in list_of_posts]
post = reddit_posts[random.randint(0,24)]
img_url = post.url
out_dir = '$PATH_TO_WALLPAPER_DIRECTORY'
r = requests.get(img_url, stream=True)
if r.status_code != 200:
    raise RuntimeError("Image didn't load")

img = Image.open(io.BytesIO(r.content))
img_hash = str(imagehash.average_hash(img))
with open('/Users/jamesshapiro/wallpaper/hashes', 'r') as f:
    data = f.read()
hashed_images = simplejson.loads(data)
if img_hash in hashed_images:
    full_path = os.path.join(out_dir, hashed_images[img_hash])
else:
    img_ext = os.path.splitext(img_url)
    st = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d-%H-%M-%S')
    img_path = 'image-{}{}'.format(st, img_ext[1])
    full_path = os.path.join(out_dir, img_path)
    img.save(full_path, quality=100)
    hashed_images[img_hash] = img_path
    dict_to_string = simplejson.dumps(hashed_images)
    with open('/Users/jamesshapiro/wallpaper/hashes', 'w') as f:
        f.write(dict_to_string)

se = app('System Events')
desktops = se.desktops.display_name.get()
for d in desktops:
    desk = se.desktops[d]
    desk.picture.set(mactypes.File(full_path))



