'''
pydub_commands.py

Useful pydub commands for manipulating audio.

Taken directly from pydub documentation here:
https://github.com/jiaaro/pydub
'''

from pydub import AudioSegment

song = AudioSegment.from_wav("never_gonna_give_you_up.wav")
# pydub does things in milliseconds
ten_seconds = 10 * 1000
first_10_seconds = song[:ten_seconds]
last_5_seconds = song[-5000:]
# boost volume by 6dB
beginning = first_10_seconds + 6
# reduce volume by 3dB
end = last_5_seconds - 3
# combine segments
without_the_middle = beginning + end
# 1.5 second crossfade
with_style = beginning.append(end, crossfade=1500)
# repeat the clip twice
do_it_over = with_style * 2
# 2 sec fade in, 3 sec fade out
awesome = do_it_over.fade_in(2000).fade_out(3000)
# export .mp3 
awesome.export("mashup.mp3", format="mp3")
