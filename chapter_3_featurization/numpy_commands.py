'''
numpy_commands.py

Quick overview of some basic numpy commands.

Although this was done in the IDLE3 window, I have commented
out those sections so you can follow along.
'''
import numpy as np

# convert a list into an array 
g=[5,2,61,1]
type(g)
g=np.array(g)
type(g)

# index an array 
g[0]

# serialize array data into .json database
# note you need to make numpy data into a list before allowing it to be
# stored in .JSON 
import json

data={
    'data':g.tolist(),
    }
jsonfile=open('test.json','w')
json.dump(data,jsonfile)
jsonfile.close()

# load .json data and make the list back into a numpy array 
newdata=json.load(open('test.json'))
numpydata=np.array(newdata['data'])
type(numpydata)
print(numpydata)

# get shape and size of numpy array
numpydata.shape
numpydata.size

# get mean, std, min, and max of numpy array 
np.mean(numpydata)
np.std(numpydata)
np.amin(numpydata)
np.amax(numpydata)

# make zeros 
makezeros=np.zeros(5)
print(makezeros)

# array operations (add, subtract, multiply by scalar)
A=np.zeros(4)
# add
print(A+numpydata)
# substract
print(A-np.array([2,-1,5,8]))
# multiply by scalar 
print(5*numpydata)
