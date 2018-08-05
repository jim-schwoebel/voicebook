'''
mongo_commands.py

Taken from the pymongo documentation

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
