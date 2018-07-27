# Install dependencies
import os

def install(modules):
  for i in range(len(modules)):
      os.system('pip3 install %s'%(modules[i]))

modules=['scikit-learn','tpot','numpy','nltk', 'SpeechRecognition',
        'spacy', 'librosa', 'TextBlob', 'matplotlib','bokeh',
        'tensorflow','keras','textgenrnn', 'sumy', 'vpython']
install(modules)

# things that need some custom setup 
os.system('brew install opus') 
os.system('brew install portaudio')
os.system('brew install sox')
os.system('python3 -m spacy.en.download all')
os.system("python3 -m spacy download 'en_core_web_sm'")
# download all nltk packages 
import nltk
nltk.download()
