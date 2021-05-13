from app import app, db, mail
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_mail import Message
from werkzeug.security import check_password_hash
from app.forms import UserInfoForm, LoginForm, PostForm
from app.models import User, Post

@app.route('/')
def index():
    context = {
       'title': 'HOME',
       'posts': Post.query.all()
    }
    return render_template('index.html', **context)


@app.route('/createpost', methods=['GET', 'POST'])
@login_required
def createpost():
    title = 'CREATE POST'
    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():
        post_title = form.title.data
        post_body = form.body.data
        user_id = current_user.id

        new_post = Post(post_title, post_body, user_id)

        db.session.add(new_post)
        db.session.commit()

        flash(f"You have created a post: {post_title}", 'info')

        return redirect(url_for('index'))

    return render_template('createpost.html', title=title, form=form)
