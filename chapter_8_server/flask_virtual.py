'''
flask_virtual.py

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
os.system('pip3 install uwsgi flask')

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

#########################################################
##	              CONFIGURE uWSGI                      ##
#########################################################

## FOR DEBUGGING 
# # test uWSGI serving 
# os.system('uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi')
# # When you have confirmed that it's functioning properly, press CTRL-C in your terminal window.

# We're now done with our virtual environment, so we can deactivate it:
os.system('deactivate')

# Next, we'll make a uwsgi configuration file. Paste this in the file terminal and save/close.
os.system('open %s'%(homedir+'/data/flask_setup/uwsgi.txt'))
os.system('nano %s/%s.ini'%(flaskdir,foldername))
'''
[uwsgi]
module = wsgi

master = true
processes = 5

socket = myproject.sock
chmod-socket = 660
vacuum = true

die-on-term = true
'''

#########################################################
##	              Systemd service unit file            ##
#########################################################

os.system('open %s'%(homedir+'/data/flask_setup/systemd.txt'))
os.system('sudo nano /etc/systemd/system/%s.service'%(foldername))

# Inside, we'll start with the [Unit] section, which is used to specify metadata and dependencies. 
# We'll put a description of our service here and tell the init system to only start this after 
# the networking target has been reached:

'''
[Unit]
Description=uWSGI instance to serve myproject
After=network.target

[Service]
User=user
Group=nginx
WorkingDirectory=/home/user/myproject
Environment="PATH=/home/user/myproject/myprojectenv/bin"
ExecStart=/home/user/myproject/myprojectenv/bin/uwsgi --ini myproject.ini

[Install]
WantedBy=multi-user.target
'''

# make sure the project is enabled and starts at boot process 
os.system('sudo systemctl start %s'%(foldername))
os.system('sudo systemctl enable %s'%(foldername))

#########################################################
##	     Configuring Nginx to Proxy Requests           ##
#########################################################

# need to configure NGINX config file now
print('IMPORTANT VARIABLES TO ADD IN\n')
print('uwsgi_pass_unix:%s'%(homedir+'/'+foldername+'/%s.sock'%(foldername)))
os.system('open %s'%(homedir+'/data/flask_setup/nginx.txt'))
os.system('sudo nano /etc/nginx/nginx.conf')

# Open up a server block just above the other server {} block that is already in the file and 
# add in the following info (uwsgi pass needs to be set to right directory

'''
http {
    . . .

	server {
	    listen 80;
	    server_name server_domain_or_IP;
	}

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/user/myproject/myproject.sock;
    }
    . . .
=
'''

# The nginx user must have access to our application directory in order to access the socket file there. 
# By default, CentOS locks down each user's home directory very restrictively, so we will add the nginx user to our 
# user's group so that we can then open up the minimum permissions necessary to grant access
os.system('sudo usermod -a -G %s nginx'%(getpass.getuser()))
# Now, we can give our user group execute permissions on our home directory. This will allow the Nginx process to enter and access content within:
os.system('chmod 710 %s'%(flaskdir))
# test nginx config file for syntax errors
os.system('sudo nginx -t')
# If this returns without indicating any issues, we can start and enable the Nginx process so that it starts automatically at boot:
os.system('sudo systemctl start nginx')
os.system('sudo systemctl enable nginx')

#########################################################
##	                LIVE SERVER!!                      ##
#########################################################
# You should now be able to go to your server's domain name or IP address in your web browser and see your application:
#os.system('open %s')

