*This section documents all the scripts in the Chapter_8_server folder.*

## Chapter 8 setup instructions

This is the only chapter with custom installation requirements. Here are some step-by-step instructions on how to install and configure everything.

### MongoDB 
You can instal mongodb with homebrew:
```
brew install mongodb
mkdir -p /data/db
sudo chmod 777 /data/db
```
All you need to run a local server is to type in this into the CLI:
```
mongod
```

### Kafka
You can install kafka with homebrew:
```
brew install kafka
```
To run a kafka server all you need to do is:
```
# run zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# run kafka 
bin/kafka-server-start.sh config/server.properties 
```

### Robo 3T 
You can install Robo 3T directly from website: https://robomongo.org/download

### Docker  
You can install Docker directly from website: https://docs.docker.com/docker-for-mac/install/

### Kubernetes
To install kubernetes, use homebrew:
```
brew install kubernetes-cli
```
To run kubernetes:
```
kubectl run [imagename]
```

### Google cloud SDK
You can install the Google Cloud SDK download and follow instructions on website: https://cloud.google.com/sdk/docs/quickstart-macos

## Python web frameworks 
### flask server
flask_project.py
```python3
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    application.run(host='0.0.0.0')
```
### django server
django_server.py
```python3
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
```
## MongoDB databases 
Here are some ways to use the pymongo module:
```python3
import pymongo
from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId

####################################################
##               MAKING MONGO CLIENT              ##
####################################################
# check server status
client = MongoClient()
client = MongoClient('localhost', 27017)
# or client = MongoClient('mongodb://localhost:27017/')
print(db.command('serverStatus'))

####################################################
##               MAKE TEST DATABASE               ##
####################################################

# make a test database
print('made test database') 
db = client.test_database
db = client['test-database']

####################################################
##               INSERT DATA IN DB               ##
####################################################
post = {"author": "Mike",
       "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}


posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)
print(post)

new_posts = [{"author": "Mike",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime.datetime(2009, 11, 12, 11, 14)},
             {"author": "Eliot",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              "date": datetime.datetime(2009, 11, 10, 10, 45)}]

result=posts.insert_many(new_posts)
print(result.inserted_ids)
print(new_posts)

####################################################
##           LIST ALL COLLECTIONS IN DB           ##
####################################################

print(db.collection_names(include_system_collections=False))


####################################################
##           INDEXING / FINDING BY IDs            ##
####################################################

# first document
print(posts.find_one())
# a specific request
posts.find_one({"author": "Eliot"})
# note that posts.find_one({“_id”:str(post_id)})) will not work 
posts.find_one({"_id":post_id})

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})

####################################################
##           COUNTING NUMBER OF DOCS IN DB       ##
####################################################
    
posts.count()
posts.find({"author":"Mike"}).count()

####################################################
##           SORT DOCS VIA EXPRESSIONS            ##
####################################################

d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
    print(post)

####################################################
##           CUSTOM SCHEMAS TO HAVE UNIQUENESS    ##
####################################################
    
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)],
                                                    unique=True)
sorted(list(db.profiles.index_information()))
user_profiles = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Ziltoid'}]
result = db.profiles.insert_many(user_profiles)
new_profile = {'user_id': 213, 'name': 'Drew'}
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
# This is fine.
result = db.profiles.insert_one(new_profile)  
# Results in error 
result = db.profiles.insert_one(duplicate_profile)
```
## Building kafka microservices  
### making a consumer
kakfa_consumer.py
```python3
from kafka import KafkaConsumer

topic='test'
consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092')

# creates a running loop to listen for messages 
for msg in consumer:
	print(msg)
```
### making a producer 
kafka_producer.py
```python3
from kafka import KafkaProducer
import time 

producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic='test'

for i in range(30):
	print('sending message...%s'%(str(i)))
	producer.send(topic, b'test2')
	time.sleep(1)

print(producer.metrics())
```
## Minio as a wrapper for GCP/AWS
minio.py
```python3
# Import Minio library.
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)

# Initialize minioClient with an endpoint and access/secret keys.
minioClient = Minio('play.minio.io:9000',
                    access_key='Q3AM3UQ867SPQQA43P2F',
                    secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
                    secure=True)

# Make a bucket with the make_bucket API call.
try:
       minioClient.make_bucket("maylogs", location="us-east-1")
except BucketAlreadyOwnedByYou as err:
       pass
except BucketAlreadyExists as err:
       pass
except ResponseError as err:
       raise
else:
        # Put an object 'pumaserver_debug.log' with contents from 'pumaserver_debug.log'.
        try:
               minioClient.fput_object('maylogs', 'pumaserver_debug.log', '/tmp/pumaserver_debug.log')
        except ResponseError as err:
               print(err)
```
## Authentication with Auth0 
auth0.py
```python3
from auth0.v3.authentication import GetToken
from auth0.v3.management import Auth0

# obtain a management token 
domain = 'myaccount.auth0.com'
non_interactive_client_id = 'exampleid'
non_interactive_client_secret = 'examplesecret'

get_token = GetToken(domain)
token = get_token.client_credentials(non_interactive_client_id,
    non_interactive_client_secret, 'https://{}/api/v2/'.format(domain))
mgmt_api_token = token['access_token']

# use your management token 
auth0 = Auth0(domain, mgmt_api_token)

#The Auth0() object is now ready to take orders! Let's see how we can use this to get all available connections. (this action requires the token to have the following scope: read:connections)
print(auth0.connections.all())
```
## Working with docker containers  
Check out this [docker and python intro talk](https://www.youtube.com/watch?v=VhabrYF1nms).

## Unit test and integration tests 
unit_test.py
```python3
import unittest

class SimplisticTest(unittest.TestCase):

    def test(self):
        a = 'a'
        b = 'a'
        self.assertEqual(a, b)
 
if __name__ == '__main__':
    unittest.main()
```
## Resources
If you are interested to read more on any of these topics, check out the documentation below.

**Web frameworks** 
* [Flask](http://flask.pocoo.org/)
* [Django](https://www.djangoproject.com/)
* [Nginx](https://www.fullstackpython.com/nginx.html)
* [Gunicorn](http://gunicorn.org/)
* [Uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html)
* [Virtualenv](https://virtualenv.pypa.io/en/stable/) 
* [ReST API / Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
* [Jinja (.HTML formatting)](http://jinja.pocoo.org/docs/2.10/intro/#basic-api-usage) 
* [Postman (GET/POST requests)](https://www.getpostman.com/docs/v6/)

**Databases**
* [Flask-pymongo](https://flask-pymongo.readthedocs.io/en/latest/ Pip3 install flask-pymongo)
* [Pymongo (mongoDB)](https://api.mongodb.com/python/current/)
* [Pyycopg (postgres)](http://initd.org/psycopg/)
* [Sqlite3 (sqlite)](https://docs.python.org/2/library/sqlite3.html) 
* [Json](https://developer.rhino3d.com/guides/rhinopython/python-xml-json/)
* [Robo 3T](https://robomongo.org/)

**Kafka microservices**  
* [Kafka and python tutorial](http://www.admintome.com/blog/kafka-python-tutorial-for-fast-data-architecture/)
* [Kafka-python](http://kafka-python.readthedocs.io/en/master/)

**File storage** 
* [Minio (offline)](https://github.com/minio/minio-py)
* [AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
* [Google cloud storage](https://cloud.google.com/storage/)

**Containers** 
* [Docker](https://cloud.google.com/storage/) 
* [Docker and python intro talk](https://www.youtube.com/watch?v=VhabrYF1nms)

**Authentication** 
* [Auth0](https://github.com/auth0/auth0-python)

**Unit and integration tests** 
* [Unittest() framework](https://docs.python.org/3/library/unittest.html) 
* [Pytest](https://docs.pytest.org/en/latest/)

**Deploying software applications** 
* [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)
* [Kubernetes](https://github.com/kubernetes/kubernetes)
* [GCP Kubernetes Engine documentation](https://cloud.google.com/kubernetes-engine/docs/)
* [Github cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf) 
