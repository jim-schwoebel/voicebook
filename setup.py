'''
setup.py

Custom script to install dependencies for voicebook.

Requires homebrew to be installed on endpoint device
and assumes an iOS operating system.

'''
# Install dependencies
import os

def install(modules):
  for i in range(len(modules)):
      os.system('pip3 install %s'%(modules[i]))

# things that need some custom setup 
os.system('brew install opus') 
os.system('brew install portaudio')
os.system('brew install sox')
os.system('brew install nginx')
os.system('pip3 install --upgrade setuptools')
os.system('pip3 install -U pyobjc')

modules=['scikit-learn','tpot','numpy','nltk', 'SpeechRecognition',
        'spacy', 'librosa', 'TextBlob', 'matplotlib','bokeh',
        'tensorflow','keras','textgenrnn', 'sumy', 'drawnow',
        'matplotlib','seaborn', 'scipy', 'wordcloud', 'pybluez',
        'wireless', 'pyserial', 'flask', 'django', 'uwsgi',
        'virtualenv']

install(modules)

os.system('python3 -m spacy.en.download all')
os.system("python3 -m spacy download 'en_core_web_sm'")
# download all nltk packages 
import nltk
nltk.download()
