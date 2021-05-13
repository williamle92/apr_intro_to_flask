from app import db
from flask import current_app as app, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.forms import PostForm
from app.models import Post

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
