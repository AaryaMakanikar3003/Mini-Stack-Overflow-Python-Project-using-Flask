from flask import Flask, render_template, Blueprint, flash, redirect, request, url_for, session
from app.models.questionModel import Question
from datetime import datetime
from bson.objectid import ObjectId

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
            'created_at': datetime.utcnow(),
            'username': session.get('username')
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

@question_bp.route('/questions/<question_id>') 
def question_detail(question_id):
    question=Question.get_question_by_id(question_id)
    return render_template(
        'questionDetails.html',
        question=question
    )
    
@question_bp.route('/add-answer/<question_id>', methods=['POST', 'GET'])
def add_answer(question_id):
    answer_text=request.form.get('answer')
    
    answer_data={
        'answer':answer_text,
        'username':session.get('username')
    }
    
    Question.add_answer(question_id, answer_data)
    
    return redirect(url_for(
        'question.question_detail',
        question_id=question_id
    ))