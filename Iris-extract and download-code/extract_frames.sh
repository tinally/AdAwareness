rest=Thumb%03d.png

mkdir -p frames

count=0

for filename in ./videos/*; do

    count=`expr $count + 1` #incrementation

	SUBSTRING=$(echo "$filename"| cut -d'/' -f 3| cut -d'.' -f 1)
	echo $SUBSTRING

	path=./frames/"$SUBSTRING"

	mkdir -p -- "$path"
	
    echo "$filename"; # include spaces
  
    ffmpeg -i "$filename" -vf  "select=gt(scene\,0.15), scale=640:360" -vsync vfr "$path"/$count$rest;
    done
