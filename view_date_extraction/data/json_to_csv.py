
import json
import csv

from ast import literal_eval



with open('8m.csv', 'w') as csvfile: 
	filewriter = csv.writer(csvfile, delimiter=',')


	with open('8m.json') as jsonfile:
	    for raw in jsonfile:
	    	python_dict = literal_eval(raw)
	    	print(python_dict)
	    	# result = json.loads(raw)

	    	# video_id = result['video_id']
	    	# viewCount = result['viewCount']
	    	# # description = result['description']


	    	# filewriter.writerow([video_id, viewCount])
