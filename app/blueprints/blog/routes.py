from . import bp as blog
from app import db
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .forms import PostForm
from .models import Post


@blog.route('/createpost', methods=['GET', 'POST'])
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


@blog.route('/myposts')
@login_required
def myposts():
    title = 'MY POSTS'
    posts = Post.query.filter_by(user_id=current_user.id).all()
    return render_template('myposts.html', title=title, posts=posts)


@blog.route('/posts/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    title = f'{post.title}'
    return render_template('post_detail.html', title=title, post=post)
