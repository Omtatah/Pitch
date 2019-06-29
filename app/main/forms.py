from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import StringField, TextAreaField, SubmitField, RadioField, SelectField


class PostCommentForm(FlaskForm):
    comment = TextAreaField('Write a comment')
    submit = SubmitField('Comment')


class PostPitchForm(FlaskForm):
    category = SelectField('Select the category', choices=[('Religion', 'Religion'), (
        'General', 'General'), ('Educative', 'Educative'), ('Inspirational', 'Inspirational')])
    text = TextAreaField('Type your pitch'),
    submit = SubmitField('Post')
