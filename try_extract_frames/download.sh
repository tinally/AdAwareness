# a shell program that downloads all the youtube videos from a txt file. 
# each url in the txt file should be on a separate line

# usage: ./download.sh <the name of the txt file>

# txt file format:
	# gm_n76Dsl0c
	# QXAYIYdvnys
	# onPZIVemXKQ
	# -T7zyezBkuY
	# e01a4-ClcTs
	# zwY6acYYO3o

youtube=http://www.youtube.com/watch?v=
mkdir -p videos

while read line
do
    name=$line

    echo "Text read from file - $name"
    youtube-dl -o "./videos/%(title)s.%(ext)s" -f 18 "$youtube$name"
done < $1