# ./batch_label_nudity.sh
mkdir -p labels

mkdir -p labels/deepAI

# store the filenames in a list

for filename in ./frames/*; do
	for image in "$filename"/*.png; do

		echo "$image"

		SUBSTRING=$(echo "$filename"| cut -d'/' -f 3| cut -d'.' -f 1)
		echo $SUBSTRING

		# touch -a labels/deepAI/"$SUBSTRING".txt

		python deepAI_nudity_detector.py -f "$image" >> labels/deepAI/"$SUBSTRING".txt

		done
	done