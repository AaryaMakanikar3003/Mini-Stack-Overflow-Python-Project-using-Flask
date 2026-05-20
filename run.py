from app import create_app
import os

app=create_app()
app.config['UPLOAD_FOLDER']='app/static/uploads'

app.secret_key='mini_stack_secret'

if __name__=='__main__':
    app.run(debug=True)