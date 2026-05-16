from flask import Flask

def create_app():
    app=Flask(__name__)
    
    app.secret_key = "supersecretkey"
    
    from app.routes.homeRoute import home_bp
    app.register_blueprint(home_bp)
    
    from app.routes.authRoute import auth_bp
    app.register_blueprint(auth_bp)
    
    from app.routes.questionRoute import question_bp
    app.register_blueprint(question_bp)
    
    from app.database.db import db

    return app

