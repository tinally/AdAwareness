# process the raw txt data 
python process_raw.py -f video_ids.txt
# download all the videos listed in the clean txt data version
# put all the videos inside the folder videos
./download.sh video_ids_clean.txt
# extract all the frames
# put all the frames in the folder named after the video title. The folder is then placed under "frame" folder
./extract_frames.sh