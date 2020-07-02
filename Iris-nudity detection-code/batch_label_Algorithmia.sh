# ./batch_label_nudity.sh
mkdir -p labels

mkdir -p Algo

# store the filenames in a list

for filename in ./frames/*; do
	for image in "$filename"/*.png; do

		echo "$image"

		SUBSTRING=$(echo "$filename"| cut -d'/' -f 3| cut -d'.' -f 1)
		echo $SUBSTRING

		python deepAI_nudity_detector.py -f "$image" >> labels/Algo/"$SUBSTRING".txt

		done
	done