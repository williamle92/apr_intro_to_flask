from app import app
from flask import render_template, request
from app.forms import UserInfoForm

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


@app.route('/register', methods=['GET', 'POST'])
def register():
    title = 'REGISTER'
    form = UserInfoForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(username, email, password)

    return render_template('register.html', title=title, form=form)