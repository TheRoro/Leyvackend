from pymongo import MongoClient
import os

mongol_user = os.environ.get("mongol_user")
mongol_password = os.environ.get("mongol_password")


client = MongoClient(
    f"mongodb+srv://{mongol_user}:{mongol_password}@one-piece.gskyyi1.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db

collection_name = db["todo_collection"]
