from app import app
from flask import render_template

@app.route('/')
def index():
    context = {
       'title': 'HOME',
       'items': ['apple', 'banana', 'orange', 'pear', 'watermelon', 'grapefruit', 'grapes'],
       'user': {
            'id': 2,
            'username': 'Brian'
        }  
    }
    return render_template('index.html', **context)


@app.route('/register')
def register():
    title = 'REGISTER'
    return render_template('register.html', title=title)