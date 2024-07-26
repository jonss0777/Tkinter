from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from credentials import cred

# Getting credentials
uri = cred()

def connectToDatabase(collectionName):
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client    