'''
change_volume.py

Changes volume by a scale input by user.
'''
import os

def change_volume(filename, vol):
    # rename file
    if vol > 1:
        new_file=filename[0:-4]+'_increase_'+str(vol)+'.wav'
    else:
        new_file=filename[0:-4]+'_decrease_'+str(vol)+'.wav'

    # changes volume, vol, by input 
    os.system('sox -v %s %s %s'%(str(vol),filename,new_file))

    return new_file 

# increase volume by 2x 
new_file=change_volume('5.wav', 2)
# decrease volume by 1/2 
new_file=change_volume('5.wav', 0.5)