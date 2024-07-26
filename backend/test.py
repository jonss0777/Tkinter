from database import connectToDatabase

collectionName = "sample_users"
databaseName  = "sample_users"



# Getting user ID aka primary key
def getUserId(username):
    try:
        client = connectToDatabase()
        db = client[databaseName]
        collection = db[collectionName]
        userId = collection.find({"username": username})
        return userId
    except Exception as e:
        print(f"Error: {e}") 
    finally:
    # Close the MongoDB client if it was initialized
        if client is not None:
            client.close()
            print("Connection closed.")


# creating a collection 
def createCollection(collectionName):
    try:
        client = connectToDatabase()
        db = client[databaseName]
        list_of_collections = db.list_collection_names()
        if collectionName not in list_of_collections:
            collection = db[collectionName]
            print("Collection created")
        else:
            print("Collection already exists")

    except Exception as e:
        print(f"Error: {e}") 
    finally:
    # Close the MongoDB client if it was initialized
        if client is not None:
            client.close()
            print("Connection closed.")


# Inserting data
def insertUserDataToCollection(data):
    try:
        client = connectToDatabase()
        db = client[databaseName]
        collection = db[collectionName]
        sid = collection.insert_one(data).inserted_id
        print(f"Data inserted with ID: {sid}")
    except Exception as e:
        print(f"Error: {e}") 
    finally:
    # Close the MongoDB client if it was initialized
        if client is not None:
            client.close()
            print("Connection closed.")


# Update data
def updateUserDataFromCollection(username, data):
    try:
        client = connectToDatabase()
        db = client[databaseName]
        collection = db[collectionName]
        sid = getUserId(username)
        collection.update_one({'_id':sid}, {"$set":data})
        print("Updated data")
    except Exception as e:
        print(f"Error: {e}") 
    finally:
    # Close the MongoDB client if it was initialized
        if client is not None:
            client.close()
            print("Connection closed.")

# Fetch data
def  getUserDataFromCollection():
    try:
        client = connectToDatabase()
        db = client[databaseName]
        collection = db[collectionName]
        collection.find({})
        print("Successfully retrieved data")
    except Exception as e:
        print(f"Error: {e}") 
    finally:
    # Close the MongoDB client if it was initialized
        if client is not None:
            client.close()
            print("Connection closed.")

# Delete Data

def delUserDataFromCollection(username):
    try:
        client = connectToDatabase()
        db = client[databaseName]
        collection = db[collectionName]
        sid = getUserId(username)
        collection.delete_one({'_id':sid})
        print("Successfully deleted data")
    except Exception as e:
        print(f"Error: {e}") 
    finally:
    # Close the MongoDB client if it was initialized
        if client is not None:
            client.close()
            print("Connection closed.")