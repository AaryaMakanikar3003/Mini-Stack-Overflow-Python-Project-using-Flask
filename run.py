from app import create_app

app=create_app()

app.secret_key='mini_stack_secret'

if __name__=='__main__':
    app.run(debug=True)