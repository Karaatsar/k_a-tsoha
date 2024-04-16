from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
import os

def login(username, password):
    sql = "SELECT id, password FROM users WHERE name=:username"
    result = db.session.execute(sql, {"name":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["username"]

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)

def user_id():
    return session.get("user_id",0)

def get_username(user_id):
    sql = "SELECT username FROM users WHERE id = : user_id"
    result = db.session.execute(sql, {"user_id": user_id})
    username = result.fetchone()[0]
    return username
