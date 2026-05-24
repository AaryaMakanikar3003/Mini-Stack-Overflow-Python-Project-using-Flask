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
        
    @staticmethod
    def upvote_question(question_id):
        return questions_collection.update_one(
            {
                '_id':ObjectId(question_id)
            },
            {
                '$inc':{
                    'votes':1
                }
            }
        )
        
    @staticmethod
    def downvote_question(question_id):
        return questions_collection.update_one(
            {
                '_id': ObjectId(question_id)
            },
            {
                '$inc': {
                    'votes': -1
                }
            }
        )
        
    @staticmethod
    def search_questions(search_text):

        return list(
            questions_collection.find(
                {
                    '$or': [
                        {
                            'title': {
                                '$regex': search_text,
                                '$options': 'i'
                            }
                        },
                        {
                            'description': {
                                '$regex': search_text,
                                '$options': 'i'
                            }
                        },
                        {
                            'tags': {
                                '$regex': search_text,
                                '$options': 'i'
                            }
                        }
                    ]
                }
            ).sort('_id', -1)
        )
        
    @staticmethod
    def accept_answer(question_id, answer_index):
        question = questions_collection.find_one({
        '_id': ObjectId(question_id)
        })

        answers = question['answers']

        for answer in answers:
            answer['is_accepted'] = False

        answers[answer_index]['is_accepted'] = True
 
        return questions_collection.update_one(
            {
                '_id': ObjectId(question_id)
            },
            {
                '$set': { 
                    'answers': answers
                }
            }
        ) 