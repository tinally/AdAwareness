# a shell program that downloads all the youtube videos from a txt file. 
# each url in the txt file should be on a separate line

# -o "~/Desktop/%(title)s.%(ext)s"  set the directory for download

!/bin/bash
youtube=http://www.youtube.com/watch?v=
while read line
do
    name=$line

    echo "Text read from file - $name"
    youtube-dl -f 18 "$youtube$name"
done < $1