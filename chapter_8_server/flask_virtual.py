'''
================================================ 
##            VOICEBOOK REPOSITORY            ##      
================================================ 

repository name: voicebook 
repository version: 1.0 
repository link: https://github.com/jim-schwoebel/voicebook 
author: Jim Schwoebel 
author contact: js@neurolex.co 
description: a book and repo to get you started programming voice applications in Python - 10 chapters and 200+ scripts. 
license category: opensource 
license: Apache 2.0 license 
organization name: NeuroLex Laboratories, Inc. 
location: Seattle, WA 
website: https://neurolex.ai 
release date: 2018-09-28 

This code (voicebook) is hereby released under a Apache 2.0 license license. 

For more information, check out the license terms below. 

================================================ 
##               LICENSE TERMS                ##      
================================================ 

Copyright 2018 NeuroLex Laboratories, Inc. 

Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at 

     http://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License. 

================================================ 
##               SERVICE STATEMENT            ##        
================================================ 

If you are using the code written for a larger project, we are 
happy to consult with you and help you with deployment. Our team 
has >10 world experts in Kafka distributed architectures, microservices 
built on top of Node.js / Python / Docker, and applying machine learning to 
model speech and text data. 

We have helped a wide variety of enterprises - small businesses, 
researchers, enterprises, and/or independent developers. 

If you would like to work with us let us know @ js@neurolex.co. 

================================================ 
##            FLASK_VIRTUAL.PY                ##    
================================================ 

Make flask in a virtual environment in the current directory.

Following along the tutorial here:
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-centos-7
'''
import os, virtualenv, getpass

#########################################################
##				MAKE VIRTUAL ENVIRONMENT               ##
#########################################################

homedir=os.getcwd()
foldername='flask_virtual'

os.mkdir(foldername)
os.chdir(foldername)
flaskdir=os.getcwd()
            
# This will install a local copy of Python and pip into a directory called myprojectenv within your project directory.
os.system('virtualenv %senv'%(foldername))

# Before we install applications within the virtual environment, we need to activate it. You can do so by typing:
os.system('source %senv/bin/activate'%(foldername))

# Your prompt will change to indicate that you are now operating within the virtual environment. 
# It will look something like this (flask_virtualenv)user@host:~/myproject$.

#########################################################
##	      CREATE FLASK VIRTUAL ENVIRONMENT.            ##
#########################################################

# install uwsgi and flask modules (and anything else you neeed for your app)
os.system('pip3 install gunicorn flask')

 # Paste this code inside the file
os.system('open %s'%(homedir+'/data/flask_setup/flask.txt'))

# create flask app in a single file 
os.system('nano %s/%s.py'%(flaskdir,foldername))

# Within this file, we'll place our application code. Basically, we need to import flask and instantiate a Flask object. 
# We can use this to define the functions that should be run when a specific route is requested. We'll call our Flask 
# application in the code application to replicate the examples you'd find in the WSGI specification:

'''
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    application.run(host='0.0.0.0')
'''
os.system('python3 %s.py'%(foldername))

# Visit your server's domain name or IP address followed by the port number specified in the terminal output 
# (most likely :5000) in your web browser. You should see something like this: "Hello World"

# When you are finished, hit CTRL-C in your terminal window a few times to stop the Flask development server.


#########################################################
##	      Create the WSGI Entry Point.                 ##
#########################################################
os.system('open %s'%(homedir+'/data/flask_setup/wsgi.txt'))
os.system('nano %s/wsgi.py'%(flaskdir))

# insert this code inside the wsgi file
# Save and close the file when you are finished.
'''
from myproject import application

if __name__ == "__main__":
    application.run()
'''

## FOR DEBUGGING 
# # test uWSGI serving 
# os.system('uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi')
# # When you have confirmed that it's functioning properly, press CTRL-C in your terminal window.
os.system('gunicorn --bind 0.0.0.0:8000 wsgi')

# We're now done with our virtual environment, so we can deactivate it:
os.system('deactivate')


#########################################################
##	              CONFIGURE uWSGI                      ##
#########################################################

# Next, we'll make a uwsgi configuration file. Paste this in the file terminal and save/close.
os.system('open %s'%(homedir+'/data/flask_setup/gunicorn.txt'))
os.system('sudo nano /etc/init/%s.conf'%(foldername))
'''
description "Gunicorn application server running myproject"

start on runlevel [2345]
stop on runlevel [!2345]

respawn
setuid user
setgid www-data

env PATH=/home/user/myproject/myprojectenv/bin
chdir /home/user/myproject
exec gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi
'''
os.system('sudo start %s'%(foldername))

#########################################################
##	     Configuring Nginx to Proxy Requests           ##
#########################################################

# configure nginx
os.system('sudo nano /etc/nginx/sites-available/%s'%(foldername))

# Open up a server block just above the other server {} block that is already in the file and 
# add in the following info (uwsgi pass needs to be set to right directory

'''
...
server {
    listen 80;
    server_name server_domain_or_IP;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/user/myproject/myproject.sock;
    }
}
...
'''

os.system('sudo ln -s /etc/nginx/sites-available/%s /etc/nginx/sites-enabled'%(foldername))
# test nginx config file for syntax errors
os.system('sudo nginx -t')
os.system('sudo service nginx restart')

#########################################################
##	                LIVE SERVER!!                      ##
#########################################################
# You should now be able to go to your server's domain name or IP address in your web browser and see your application:
#os.system('open %s')

