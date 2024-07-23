# Note: PyMongo is synchronous

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from credentials import cred

# Getting credentials
uri = cred()


# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


collection = client.sample_airbnb.listingsAndReviews

post_id = '10006546'
#print(collection)
result = collection.find_one({"_id": post_id})
print(result["listing_url"])


# Send a ping to confirm a successful connection
#try
#    client.admin.command('ping')
#    print("Pinged your deployment. You successfully connected to MongoDB!")
#except Exception as e:
#    print(e)
    

def db_register_user():
    pass

def db_login_user():
    pass

def db_get_user():
    # contains
    # username
    # password
    # description
    # rank
    # best score
    # friend_list 
    # friend_request
    pass