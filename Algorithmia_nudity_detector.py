# import nude
# from nude import Nude

# print(nude.is_nude('./nude.png'))

# n = Nude('./nude.png')
# n.parse()
# print("nude :", n.result, n.inspect())

# the output 

from __future__ import unicode_literals
import youtube_dl

import os
import io
from PIL import Image
from array import array

import sys
import os
import subprocess
import argparse
import glob
import requests
import Algorithmia
import Algorithmia
from Algorithmia.acl import ReadAcl, AclType
import json

def sending_requests(file):
	# Authenticate with your API key
	apiKey = "simQRdDhIS0JzvyNWVsqifuqXdz1"
	# Create the Algorithmia client object
	client = Algorithmia.client(apiKey)
	# Instantiate a DataDirectory object, set your data URI and call create
	nlp_directory = client.dir("data://irisong980912/nlp_directory")
	# Create your data collection if it does not exist
	if nlp_directory.exists() is False:
	    nlp_directory.create()

	# Create the acl object and check if it's the .my_algos default setting
	acl = nlp_directory.get_permissions()  # Acl object
	acl.read_acl == AclType.my_algos  # True

	# Update permissions to private
	nlp_directory.update_permissions(ReadAcl.private)
	nlp_directory.get_permissions().read_acl == AclType.private # Truetext_file = "data://irisong980912/nlp_directory/jack_london.txt"

	image_file = "data://irisong980912/nlp_directory/" + file

	if client.file(image_file).exists() is False:
	    # Upload local file
	    client.file(image_file).putFile(file)


	algo = client.algo('sfw/NudityDetectioni2v/0.2.13')

    # Download contents of file as a string
	if client.file(image_file).exists() is True:
		print("YES")
		s = '{ "image" : "' + image_file + '"}'
		input = json.loads(s)
		print(input["image"])
		algo.set_options(timeout=300)
		print(algo.pipe(input).result)

	
	# algo.set_options(timeout=300) # optional
	# print(algo.pipe(input).result)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='write the image path that you wish to process')
    parser.add_argument('-f', '--file', metavar='file', required=True,
                        help='the path to the image file')
    args = parser.parse_args()
    sending_requests(args.file)