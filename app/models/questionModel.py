from app.database.db import questions_collection
from bson.objectid import ObjectId

class Question:
    @staticmethod
    def create_question(question_data):
        return questions_collection.insert_one(question_data)
    
    @staticmethod
    def get_all_questions():
        return list(questions_collection.find().sort('_id', -1))
    
    @staticmethod
    def get_question_by_id(question_id):
        return questions_collection.find_one({
            '_id':ObjectId(question_id)
        }) 
        
    @staticmethod
    def add_answer(question_id, answer_data):
        return questions_collection.update_one(
            {
                '_id': ObjectId(question_id) 
            },
            {
                '$push': {
                    'answers': answer_data
                }
            }
        )