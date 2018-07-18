'''
transcode.py

Usef ffmpy wrapper for FFmpeg to transcode file types.
'''
import ffmpy

def convert_wav(input_file, output_file):
    #take in an audio file and convert with ffmpeg to proper file type 
    try:
        ff = ffmpy.FFmpeg(
            inputs={input_file:None},
            outputs={output_file: None}
            )
        ff.run()
    except:
    	print('error')


convert_wav('test.wav', 'test.mp3')
