# curl \
#     -F 'image=YOUR_IMAGE_URL' \
#     -H 'api-key:1ec3c1b7-bf99-44ca-a65f-cd64efcb58b0' \
#     https://api.deepai.org/api/nsfw-detector 
# given the file path
from __future__ import unicode_literals
import youtube_dl

import sys
import os
import subprocess
import argparse
import glob
import requests

def sending_requests(file):
	r = requests.post(
	    "https://api.deepai.org/api/nsfw-detector",
	    files={
	        'image': open(file, 'rb'),
	    },
	    headers={'api-key': 'c5b04f2b-a797-4c7e-be92-3845fd301036'}
	)
	print(r.json())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='write the image path that you wish to process')
    parser.add_argument('-f', '--file', metavar='file', required=True,
                        help='the path to the image file')
    args = parser.parse_args()
    sending_requests(args.file)