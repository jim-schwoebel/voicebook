'''
django_project.py

Start a django project (django_server) in current directory,
list file contents, and then launch the server.

From django tutorial here:

'''
import os

def dirtree(rootDir): 
    list_dirs = os.walk(rootDir) 
    for root, dirs, files in list_dirs: 
        for d in dirs: 
            print(os.path.join(root, d))     
        for f in files: 
            print(os.path.join(root, f))
            
# make a django project in the current directory 
os.system('django-admin startproject django_server')

print('CREATING FILES...')
print(dirtree(os.getcwd()+'/django_server'))

print('lauching server...')
os.chdir('django_server')
os.system('python3 manage.py runserver')