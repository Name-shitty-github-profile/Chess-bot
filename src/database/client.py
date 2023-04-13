from pymongo import MongoClient
from os import environ
client = MongoClient(environ['url'])
db = client['main']

def gt(collection) -> dict:
  return db[collection]
