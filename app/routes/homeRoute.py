from flask import Flask, render_template, Blueprint

home_bp=Blueprint("home_bp", __name__)

@home_bp.route('/')
def home():
    return render_template('home.html')