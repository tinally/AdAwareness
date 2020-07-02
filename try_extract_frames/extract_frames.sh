# extract keyframes of all the videos inside the "videos" folder into separate folders
# ./extract_frames.sh

rest=Thumb%03d.png

mkdir -p frames

for filename in ./videos/*.mp4; do

	SUBSTRING=$(echo "$filename"| cut -d'/' -f 3| cut -d'.' -f 1)
	echo $SUBSTRING

	path=./frames/"$SUBSTRING"

	mkdir -p -- "$path"
	
    echo "$filename"; # include spaces
  
    ffmpeg -i "$filename" -vf  "select=gt(scene\,0.15), scale=640:360" -vsync vfr "$path"/$rest;
    done