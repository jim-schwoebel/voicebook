'''
convert_wav.py

Usef ffmpy wrapper for FFmpeg to convert .mp3, .m4a, or .ogg files to .wav files
'''

def convert_wav(filename):
    #take in an audio file and convert with ffpeg file type
    #types of input files: .mp3 
    #output file type: .wav
   
    if filename[-4:] in ['.mp3','.m4a','.ogg']:
        ff = ffmpy.FFmpeg(
            inputs={filename:None},
            outputs={filename[0:-4]+'.wav': None}
            )
        ff.run()

convert_wav('test.mp3')
