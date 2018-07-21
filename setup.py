# Install dependencies
import os

os.system('brew install opus') 
os.system('brew install taglib')
os.system('python3 -m spacy.en.download all')
os.system("python3 -m spacy download 'en_core_web_sm'")
os.system('pip3 install megaman') 
