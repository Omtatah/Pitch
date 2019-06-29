from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Comment,User,Post
from flask_login import login_required, current_user
from .. import db
from .forms import PostPitchForm,PostCommentForm
import markdown2 


@main.route('/')
def index():
    return '<h1> Hello World </h1>'
