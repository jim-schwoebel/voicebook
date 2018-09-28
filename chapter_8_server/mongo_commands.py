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
##             MONGO_COMMANDS.PY              ##    
================================================ 

Taken from the pymongo documentation:
https://api.mongodb.com/python/current/
'''
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
