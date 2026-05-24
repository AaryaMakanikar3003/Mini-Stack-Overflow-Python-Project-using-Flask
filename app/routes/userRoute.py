from flask import Blueprint, render_template
from app.models.userModel import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/users/<username>')
def user_profile(username):

    user = User.find_user_by_username(username)

    user_questions = User.get_user_questions(username)

    total_answers = User.count_user_answers(username)

    accepted_answers = User.count_accepted_answers(username)

    reputation = User.calculate_reputation(username)

    return render_template(
        'profile.html',
        user=user,
        user_questions=user_questions,
        total_answers=total_answers,
        accepted_answers=accepted_answers,
        reputation=reputation
    )