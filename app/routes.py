from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import UserInfoForm
from app.models import User, Post

@app.route('/')
def index():
    context = {
       'title': 'HOME',
       'posts': Post.query.all(),
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
        # print(username, email, password)
        # Check if username/email already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).all()
        if existing_user:
            flash('That username or email already exists. Please try again', 'danger')
            return redirect(url_for('register'))
        
        new_user = User(username, email, password)
        db.session.add(new_user)
        db.session.commit()

        flash(f'Thank you {username} for registering!', 'success')
        return redirect(url_for('index'))


    return render_template('register.html', title=title, form=form)