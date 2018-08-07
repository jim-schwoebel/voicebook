'''
setup.py

Custom script to install dependencies for voicebook.

Requires homebrew to be installed on endpoint device
and assumes an iOS operating system.

'''
# Install dependencies
import os

def pip3_install(modules):
  for i in range(len(modules)):
    os.system('pip3 install %s'%(modules[i]))

def brew_install(modules):
  for i in range(len(modules)):
      os.system('brew install %s'%(modules[i]))
      
# things that need some custom setup 
os.system('pip3 install --upgrade setuptools')
os.system('pip3 install -U pyobjc')
os.system('brew install heroku/brew/heroku')
os.system('brew cask info google-cloud-sdk')

# install homebrew and pip modules 
brew_modules=['opus','portaudio','sox','nginx', 'kafka']

pip3_modules=['scikit-learn','tpot','numpy','nltk', 'SpeechRecognition',
              'spacy', 'librosa', 'TextBlob', 'matplotlib','bokeh',
              'tensorflow','keras','textgenrnn', 'sumy', 'drawnow',
              'matplotlib','seaborn', 'scipy', 'wordcloud', 'pybluez',
              'wireless', 'pyserial', 'flask', 'django', 'uwsgi',
              'virtualenv', 'minio','pymongo', 'auth0-python', 'google-cloud-storage',
              'pycrypto']

brew_install(brew_modules)
pip3_install(pip3_modules)

# customize spacy packages 
os.system('python3 -m spacy.en.download all')
os.system("python3 -m spacy download 'en_core_web_sm'")
# download all nltk packages 
import nltk 
nltk.download('all')
