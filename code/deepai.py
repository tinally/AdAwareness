from bson import json_util # pymongo
import requests
import os
import json

def json_write(file, data):
	with open(file, 'w') as f:
	    for element in data:
	    	f.write(json_util.dumps(element)+'\n')

#path = '/home/nina/ai4good/nude12.jpeg' #one picture exemple
folders = os.listdir('/home/nina/ai4good/gender_bias/frames')

results = []

for folder in folders:
	frames = os.listdir('/home/nina/ai4good/gender_bias/frames/' + folder)
	for frame in frames:

		r = requests.post(

		    "https://api.deepai.org/api/nsfw-detector",
		    files={
		        'image': open('/home/nina/ai4good/gender_bias/frames/' + folder + "/" + frame, 'rb'),
		    },
		    headers={'api-key': 'c5b04f2b-a797-4c7e-be92-3845fd301036'}
		)

		output = r.json()
		output['file'] = frame # add the name of the file
		results.append(output)
		print(frame + " - done")
		json_write('results.json', results)

	print(folder + " - done")

json_write('results.json', results)