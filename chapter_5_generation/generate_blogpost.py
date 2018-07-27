'''
generate_email.py

Take in some emails from ENRON dataset and generate some emails.
'''
import os, json
from textgenrnn import textgenrnn

# now use textgenrnn to train a model (1 epoch = faster)
os.chdir('data')
#textgen = textgenrnn('textgenrnn_weights.hdf5')
textgen=textgenrnn()
textgen.train_from_file('blogposts.txt', num_epochs=1)

# now generate new text messages
newmsgs=list()
for i in range(10):
    newmsg=textgen.generate()


    
