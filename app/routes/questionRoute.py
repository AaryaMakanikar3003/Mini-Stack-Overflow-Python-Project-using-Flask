from flask import Flask, render_template, Blueprint, flash, redirect, request, url_for
from app.models.questionModel import Question
from datetime import datetime

question_bp=Blueprint("question", __name__)

@question_bp.route('/ask-question', methods=['GET', 'POST'])
def ask_question():
    if request.method=='POST':
        title=request.form.get('title')
        description=request.form.get('description')
        tags=request.form.get('tags')
        
        question_data={
            'title':title,
            'description':description,
            'tags': tags.split(','),
            'votes': 0,
            'answers': [],
            'created_at': datetime.utcnow()
        }
        Question.create_question(question_data)

        flash("Question Posted Successfully", "success")
        return redirect(url_for('question.questions_feed'))
    return render_template('askQuestion.html')

@question_bp.route('/questions')
def questions_feed():

    questions = Question.get_all_questions()

    return render_template(
        'questions.html',
        questions=questions
    )

        