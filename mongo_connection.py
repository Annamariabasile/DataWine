from pymongo import MongoClient

def connect_to_collection():
    client = MongoClient('mongodb://localhost:27017/')
    database = client['cleaned_datawine_database']
    collection = database['wine_collection']
    return collection
