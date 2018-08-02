'''
wakeup.py

Specify which wake word engine to use and loop one time
before waking up.
'''
import os

def wakeup(wake_type):
    if wake_type == 'porcupine':
        os.system('python3 wake_porcupine.py')
    elif wake_type == 'snowboy':
        os.system('python3 wake_snow.py')
    elif wake_type == 'sphinx':
        os.system('python3 wake_pocket.py')
    else:
        # default to porcupine if don't know 
        os.system('python3 wake_porcupine.py')

os.chdir(os.getcwd()+'/nala/data/models')
wakeup('porcupine')
