from .forms import PostPitchForm, PostCommentForm
import markdown2
from .. import db
from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from . import main
from ..models import Comment, User, Post


# Views to be rendered ->

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
