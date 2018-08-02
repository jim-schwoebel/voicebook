'''
speakup.py

Speak function for nala.
'''
import os 
def speaktext(hostdir,text):
    # speak to user from a text sample (tts system)  
    curdir=os.getcwd()
    os.chdir(hostdir+'/actions') 
    os.system("python3 speak.py '%s'"%(str(text)))
    os.chdir(curdir)

speaktext(os.getcwd()+'/nala', 'hey this is awesome')
