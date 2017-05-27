import pymongo
from pprint import pprint
from pymongo import MongoClient

# add local mongo or mongodb URL
client = MongoClient('mongodb://')

db = client.everest
pic_collection = db.pic

cursor = pic_collection.find({})
for document in cursor:
    pprint(document)
