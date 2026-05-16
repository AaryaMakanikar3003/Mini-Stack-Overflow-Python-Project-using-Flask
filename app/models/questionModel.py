from app.database.db import questions_collection
from bson.objectid import ObjectId

class Question:
    @staticmethod
    def create_question(question_data):
        return questions_collection.insert_one(question_data)
    
    @staticmethod
    def get_all_questions():
        return questions_collection.find().sort('created_at', -1)
    
    @staticmethod
    def get_question_by_id(question_id):
        return questions_collection.find_one({
            '_id':ObjectId(question_id)
        }) 