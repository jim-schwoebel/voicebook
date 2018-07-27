'''
generate_text.py


'''
from textgenrnn import textgenrnn

# now use textgenrnn to train a model (1 epoch = faster)
textgen = textgenrnn()
textgen.train_from_file('textmessages.txt', num_epochs=1)

# now generate new text messages
newmsgs=list()
for i in range(10):
    newmsg=textgen.generate()



    
