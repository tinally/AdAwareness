# ./batch_label_nudity.sh
mkdir -p labels

mkdir -p labels/Algo

# store the filenames in a list

for filename in ./frames/*; do
	for image in "$filename"/*.png; do

		# echo "$image"

		# ./frames/Dyson Vacuum Cleaner Commercial/Thumb021.png

		SUBSTRING=$(echo "$filename"| cut -d'/' -f 3| cut -d'.' -f 1)

		imageTitle=$(echo "$image"| cut -d'/' -f 4| cut -d'.' -f 1)

		path=./frames/"$SUBSTRING"/"$imageTitle".png

		python Algorithmia_nudity_detector.py -p "$path" -i "$imageTitle" -f "$SUBSTRING" >> labels/Algo/"$SUBSTRING".txt

		done
	done