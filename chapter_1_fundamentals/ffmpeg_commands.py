'''
Useful FFmpeg commands

List of useful FFmpeg commands that you can run from the command
line with the os.system() module in python.

I like this method better when converting files because it is fewer
lines of code, but beware of the security risks associated with this
approach.
'''

import os
# convert audio from one file format to another 
os.system('ffmpeg -i input.mp3 output.ogg')

# extract audio from a video 
os.system('ffmpeg -i video.mp4 -vn -ab 256 audio.mp3')

# merge audio and video files
os.system('ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac -strict experimental output.mp4')

# add a cover image to audio file
os.system('ffmpeg -loop 1 -i image.jpg -i audio.mp3 -c:v libx264 -c:a aac -strict experimental -b:a 192k -shortest output.mp4')

# crop an audio file (This will create a 30 second audio file starting at 90 seconds from the original audio file without transcoding).
os.system('ffmpeg -ss 00:01:30 -t 30 -acodec copy -i inputfile.mp3 outputfile.mp3')
