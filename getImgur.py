#!/usr/bin/python
import requests
import json
import random
import time
import settings
import os
from gi.repository import Gio
from os.path import expanduser

# Replace the usernamme alien with your username, there is 2 instances, one at the bottom also.
# If you run into any problems make sure you have permissions set correctly for desktop.jpg

image = "/home/alien/apps/ImgurWallpaper/desktop.jpg"

def get_urls(subreddit):
	url = 'https://api.imgur.com/3/gallery/r/%s/' % subreddit
	print url
	headers = {'Content-Type': 'text', 'Authorization': 'Client-ID %s' % settings.CLIENT_ID}
	print headers
	try:
		subreddit_data = requests.get(url, headers=headers, verify=False)
	except:
		return "Could not collect list of images from Imgur"

	subreddit_data = subreddit_data.json()

	urls = []
	for d in subreddit_data['data']:
		urls.append(d['link'])

	return urls

time.sleep(5)

r = requests.get(random.choice(get_urls('wallpapers/new')), stream=True)
with open(image, 'w') as f:
	print f
	try:
		f.write(r.content)
		f.close()
	except:
		print "Could not write the image to desktop.jpg."

os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/alien/apps/ImgurWallpaper/desktop.jpg")
