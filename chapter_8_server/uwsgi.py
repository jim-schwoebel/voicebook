'''
uwsgi.py

Start using uWSGI to run a http server/router passing request to WSGI
applications.

Note that uWSGI is used to interface with Nginx servers to run python-
based application code.

Do not use --http when you have a frontend webserver or you are doing
some form of benchmark, use --http-socket. Read the quickstart to understand
why:  https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html
'''
import os

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]

# using flask
# uwsgi --socket 127.0.0.1:3031 --wsgi-file myflaskapp.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191
