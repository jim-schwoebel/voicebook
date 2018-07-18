'''
zipfiles.py

Quick function to compress all the contents of a folder
into a .zip file.

This is useful if you have multiple types of data that you'd
like to upload to servers, etc.
'''
import shutil 

def zipdir(folder):
    # ziph is zipfile handle
    shutil.make_archive(folder, 'zip', folder)

# assume a whole folder filled with .wav files (e.g. 10) named testdata
zipdir('testdata')
