from werkzeug.security import generate_password_hash, check_password_hash
from pymongo.errors import DuplicateKeyError
from app.db import users, collection


class UsernameTakenError(Exception):
    pass


def create_user(username, password):
    hashed = generate_password_hash(password)
    try:
        users.insert_one({"username": username, "password": hashed})
    except DuplicateKeyError:
        raise UsernameTakenError(f"Username '{username}' is already taken.")


def find_user(username):
    return users.find_one({"username": username})


def verify_user(username, password):
    user = find_user(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None


def update_password(username, new_password):
    hashed = generate_password_hash(new_password)
    users.update_one({"username": username}, {"$set": {"password": hashed}})


def user_prediction_count(username):
    return collection.count_documents({"user": username})
