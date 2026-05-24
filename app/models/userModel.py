from app.database.db import users_collection
from app.database.db import questions_collection

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
        
    @staticmethod
    def get_user_questions(username):
        return list(
        questions_collection.find(
            {
                'username': username
            }
        ).sort('_id', -1)
    )
        
    @staticmethod
    def count_user_answers(username):
        questions = questions_collection.find()

        total_answers = 0

        for question in questions:

            for answer in question.get('answers', []):

                if answer.get('username') == username:
                    total_answers += 1

        return total_answers
    
    @staticmethod
    def count_accepted_answers(username):
        questions = questions_collection.find()

        accepted_count = 0

        for question in questions:

            for answer in question.get('answers', []):

                if (
                    answer.get('username') == username
                    and
                    answer.get('is_accepted') == True
                ):
                    accepted_count += 1

        return accepted_count
    
    @staticmethod
    def calculate_reputation(username):
        questions = questions_collection.find({
            'username': username
        })

        reputation = 0

        for question in questions:
            reputation += question.get('votes', 0) * 5

        reputation += User.count_user_answers(username) * 2

        reputation += User.count_accepted_answers(username) * 10

        return reputation