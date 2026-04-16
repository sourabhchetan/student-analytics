from werkzeug.security import generate_password_hash, check_password_hash
from app.db import db

users = db["users"]

def create_user(username, password):
    hashed = generate_password_hash(password)
    users.insert_one({
        "username": username,
        "password": hashed
    })

def find_user(username):
    return users.find_one({"username": username})

def verify_user(username, password):
    user = find_user(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None