from .forms import PostPitchForm, PostCommentForm
import markdown2
from .. import db
from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from . import main
from ..models import Comment, User, Post


# Views to be rendered ->

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    posted_pitches = Post.query.filter_by(user_id=current_user.id).all()

    return render_template("profile/profile.html", user=user, pitches=posted_pitches)


@main.route('/pitches/<int:id>', methods=['GET', 'POST'])
def pitch(id):
    # getting comments for a pitch
    all_comments = Comment.query.filter_by(post_id=id).all()

    pitch = Post.query.filter_by(id=id).first()
    form = PostCommentForm()
    # from for comments
    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(pitch_comment=comment,
                              user=current_user, post_id=id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.pitch', id=pitch.id))

    return render_template('pitches.html', pitch=pitch, comment_form=form, all_comments=all_comments)


@main.route('/', methods=['GET', 'POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = "Pitch"
    pitches = Post.query.all()

    form = PostPitchForm()
    if form.validate_on_submit():
        category = form.category.data
        pitch = form.text.data

        # Updated post
        new_pitch = Post(category=category, text=pitch, user=current_user)

        # Save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('index.html', title=title, pitch_form=form, pitches=pitches)
