# Process the raw txt list file and put each url on a separate line

from __future__ import unicode_literals
import youtube_dl

import sys
import os
import subprocess
import argparse
import glob


def process_file(file):
#Accessing a text file 

	print(file)

	name_var = file.split(".")
	name = name_var[0] + "_clean.txt"
	# print(name)

	output_file = open(name,"w+")

	input_file = open(file,"r")

	#Repeat for each song in the text file
	for line in input_file:
		# print(line)
		#Let's split the line into an array called "fields" using the ", " as a separator:
		fields = line.split(", ")
		for f in fields:
			f = f[1:-1]
			# print(f)
			output_file.write(f + '\n')

	#It is good practice to close the file at the end to free up resources   
	input_file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='write the filename that you wish to process')
    parser.add_argument('-f', '--file', metavar='file', required=True,
                        help='the path to the txt file')
    args = parser.parse_args()
    process_file(args.file)