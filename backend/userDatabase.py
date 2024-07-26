from database import connectToDatabase
from pymongo import MongoClient

class UserDatabase:
    def __init__(self, db_name, collection_name):
        self.client = None
        self.db_name = db_name
        self.collection_name = collection_name
        self.connect()

    def connect(self):
        try:
            self.client = connectToDatabase()
            self.db = self.client[self.db_name]
            self.collection = self.db[self.collection_name]
        except Exception as e:
            print(f"Connection error: {e}")

    def close(self):
        if self.client is not None:
            self.client.close()
            print("Connection closed.")

    def get_user_id(self, username):
        try:
            user = self.collection.find_one({"username": username})
            if user:
                return user['_id']
            return None
        except Exception as e:
            print(f"Error: {e}")

    def create_collection(self):
        try:
            list_of_collections = self.db.list_collection_names()
            if self.collection_name not in list_of_collections:
                self.db.create_collection(self.collection_name)
                print("Collection created")
            else:
                print("Collection already exists")
        except Exception as e:
            print(f"Error: {e}")

    def insert_user_data(self, data):
        try:
            result = self.collection.insert_one(data)
            print(f"Data inserted with ID: {result.inserted_id}")
        except Exception as e:
            print(f"Error: {e}")

    def update_user_data(self, username, data):
        try:
            user_id = self.get_user_id(username)
            if user_id:
                self.collection.update_one({'_id': user_id}, {"$set": data})
                print("Updated data")
            else:
                print("User not found")
        except Exception as e:
            print(f"Error: {e}")

    def get_user_data(self):
        try:
            users = list(self.collection.find({}))
            print("Successfully retrieved data")
            return users
        except Exception as e:
            print(f"Error: {e}")

    def delete_user_data(self, username):
        try:
            user_id = self.get_user_id(username)
            if user_id:
                self.collection.delete_one({'_id': user_id})
                print("Successfully deleted data")
            else:
                print("User not found")
        except Exception as e:
            print(f"Error: {e}")

    def __del__(self):
        self.close()

# Usage
if __name__ == "__main__":
    db = UserDatabase(db_name="sample_users", collection_name="sample_users")

    # Insert user data
    db.insert_user_data({'username': 'Alice', 'age': 30})

    # Fetch user data
    users = db.get_user_data()
    print(users)

    # Update user data
    db.update_user_data('Alice', {'age': 31})

    # Delete user data
    db.delete_user_data('Alice')

    # Create a collection
    db.create_collection()
