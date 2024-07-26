from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from credentials import cred

# Getting credentials
uri = cred()

def connectToDatabase():
    # Create a new client and connect to the server
    try:
        client = MongoClient(uri, server_api=ServerApi('1'))  
        print("Connected to MongoDB")
        return client
    
    except Exception as e:
        print(f"Error: {e}")