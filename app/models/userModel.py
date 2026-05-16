from app.database.db import users_collection

class User:
    @staticmethod
    def create_user(user_data):
        return users_collection.insert_one(user_data)
    
    @staticmethod
    def find_user_by_email(email):
        return users_collection.find_one({
            'email':email
        })
        
    @staticmethod
    def find_user_by_username(username):
        return users_collection.find_one({
            'username':username
        })    