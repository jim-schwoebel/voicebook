'''
wake_porcupine.py

Use porcupine as a wakeword engine.

https://github.com/Picovoice/Porcupine#try-it-out
'''
import os

# define directories
curdir=os.getcwd()
snowdir=curdir+'/snowboy'
model_path=curdir+'/data/Nala.pmdl'

# define function 
def porcupine_detect(snowdir,model_path):
	curdir=os.getcwd()
	os.chdir(snowdir)
	os.system('python3 demo.py %s'%(model_path))
	os.chdir(curdir)

porcupine_detect(snowdir,model_path)