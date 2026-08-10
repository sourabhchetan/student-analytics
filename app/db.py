from pymongo import MongoClient, ASCENDING
from pymongo.errors import ServerSelectionTimeoutError
from app.config import Config

client = MongoClient(Config.MONGO_URI, serverSelectionTimeoutMS=5000)
db = client["studentDB"]

collection = db["predictions"]
users = db["users"]

# Enforce uniqueness at the database level so two people can never share a
# username, even under race conditions the app-level check would miss.
# Wrapped so a temporarily-unreachable DB doesn't crash app startup —
# indexes get (re)created on the next successful connection instead.
try:
    users.create_index([("username", ASCENDING)], unique=True)
    collection.create_index([("user", ASCENDING), ("time", ASCENDING)])
except ServerSelectionTimeoutError:
    pass


def check_connection():
    """Returns True if MongoDB is reachable, False otherwise."""
    try:
        client.admin.command("ping")
        return True
    except ServerSelectionTimeoutError:
        return False
