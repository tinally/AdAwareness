
# open the deep ai result face  body file. Get all the video titles which has a non-empty detections list 

# use mongodb to store the result 

import json
from pymongo import MongoClient
from pprint import pprint

def mongo_db():

	myclient = MongoClient("mongodb://localhost:27017")
	mydb = myclient["mydatabase"]

	dblist = myclient.list_database_names()
	if "mydatabase" in dblist:
		print("The database exists.")

	DeepAI = mydb["DeepAI"]

	collist = mydb.list_collection_names()
	if "DeepAI" in collist:
		print("The collection exists.")
	return DeepAI


def read_json():
	# DeepAI = mongo_db()

	client = MongoClient('mongodb://localhost:27017')
	db = client["mydatabase"]
	DeepAI = db["DeepAI"]

	db.DeepAI.remove({})

	with open('deepai_result_face_body.json') as f:
		for line in f:
			loaded_json = json.loads(line)
			detections_list = loaded_json['output']['detections']
			video_title = loaded_json['video']
			video_id = ""
			if len(video_title) > 13 and video_title[-12] == "-":
					video_id = video_title[-11:]
					video_title = video_title[:-12]

			# search mongodb dataset by the video title, if not yet, add a new one. If find, get that one
			found = DeepAI.find_one({"video_title": video_title})
			if found: 

				found["total_f_count"] += 1
				if len(detections_list) != 0: 
					found["nude_f_count"] += 1
					# iterate through the list 
					for i in range(len(detections_list)):
						label = detections_list[i]['name']
						label_list = label.split()
						label = label_list[0] #get female or male
						if label == "Female" or label == "Male":
							found[label] += 1 # update the count of frames showing female and male nudity

				DeepAI.update_one({'video_title':video_title}, {"$set": found}, upsert=True)

			# if no search result 
			else: 
				deepAI_dict = {"video_title": video_title, "video_id": video_id, "total_f_count": 0, "nude_f_count": 0, "Female": 0, "Male": 0}
				# detect nude stuff 
				deepAI_dict["total_f_count"] += 1
				if len(detections_list) != 0: 
					deepAI_dict["nude_f_count"] += 1
					# iterate through the list 
					for i in range(len(detections_list)):
						label = detections_list[i]['name']
						label_list = label.split()
						label = label_list[0] #get female or male 
						if label == "Female" or label == "Male":
							deepAI_dict[label] += 1 # update the count of frames showing female and male nudity

				x = DeepAI.insert_one(deepAI_dict)

					

if __name__ == '__main__':
	read_json()