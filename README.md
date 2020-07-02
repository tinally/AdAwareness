# AI For Good Summer Lab Project @ Montreal, QC

## Ad Awareness

Researched on gender bias in commercials from Youtube-8M dataset by creating a nudity detection tool and statistically 
analyzing the effect of presence of nudity on views.

## Instruction on how to mass download youtube videos using youtube ids and extract key frames according to scene change
Project for AI For Social Good 2019. Detect gender bias in commercials.

### Install youtube-dl: brew install youtube-dl
### Install ffmpeg: brew install ffmpeg

You can try the following steps inside the folder "try".
Execute ./batch_command.sh to perform all three steps at once and see what happens

### Step 1: convert the url list txt file into useful format (put each url on a separate line)
    
    usage: python process_raw.py -f <name of the txt>
    
    # txt file format before processing:
	    # 'gm_n76Dsl0c', 'QXAYIYdvnys', 'onPZIVemXKQ', '-T7zyezBkuY', 'e01a4-ClcTs', 'zwY6acYYO3o'

    # txt file format after processing:
        # gm_n76Dsl0c
        # QXAYIYdvnys
        # onPZIVemXKQ
        # -T7zyezBkus
        # e01a4-ClcTs
        # zwY6acYYO3o
        
### Step 2: download all the videos listed in the clean url txt version and
        put all the videos inside the folder "videos"
        
    usage: ./download.sh <name of the txt>
    
    # txt file format:
        # gm_n76Dsl0c
        # QXAYIYdvnys
        # onPZIVemXKQ
        # -T7zyezBkuY
        # e01a4-ClcTs
        # zwY6acYYO3o
        
### Step 3: extract keyframes of all the videos inside the "videos" folder into separate folders
    
    usage: ./extract_frames.sh
