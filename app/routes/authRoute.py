from flask import render_template, Blueprint, request, flash, redirect, url_for, session
from app.models.userModel import User
import bcrypt 

auth_bp=Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='POST':
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        
        existing_email=User.find_user_by_email(email)
        
        if existing_email:
            flash("Email already exists", 'error')
            return redirect(url_for('auth.login'))
        
        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        )
        
        user_data={
            'username':username,
            'email':email,
            'password':hashed_password
        }
        User.create_user(user_data)
        flash("Signup successful", 'success')
        return redirect(url_for('home_bp.home')) 
    
    return render_template('signup.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        
        existing_user=User.find_user_by_email(email)
        
        if not existing_user:
            flash("User does not exists", 'error')
            return redirect(url_for('auth.signup'))
        
        is_password_correct=bcrypt.checkpw(password.encode('utf-8'), existing_user['password'])
        
        if not is_password_correct:
            flash("Incorrect password", 'error')
            return redirect(url_for('auth.login'))
        
        session['username']=existing_user['username']
        session['email']=existing_user['email']
        flash("Login Successful", "success")
        return redirect(url_for('home_bp.home'))
    
    return render_template('login.html')