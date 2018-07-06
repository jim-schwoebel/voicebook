import pip

try:
  import kafka-python
except:
  pip.main(["install","kafka-python"])
  
try:
  import pymongo
except:
  pip.main(["install","pymongo"])
  
try:
  import importlib
except:
  pip.main(["install","importlib"])
    
try:
  import scipy
except:
  pip.main(["install","scipy"])
  
try:
  import ffmpy
except:
  pip.main(["install","ffmpy"])
  
try:
  import getpass
except:
  pip.main(["install","getpass"])
  
try:
  import pydub
except:
  pip.main(["install","pydub"])
  
try:
  import 
except:
  pip.main(["install","numpy"])
