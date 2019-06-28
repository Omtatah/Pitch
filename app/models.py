from app import db
from app import login_manager
from sqlalchemy import func
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)

    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    posts = db.relationship('Post', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref = 'user', lazy = "dynamic")
   
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'
    

class Comment(db.Model):

    __tablename__ = 'comments'

     
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    post_id=db.Column(db.Integer, db.ForeignKey('posts.id'))
    pitch_comment = db.Column(db.Text)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    
    @classmethod
    def get_comment(post_id):
        comment=Comment.query.filter_by(post_id=id)
        return comment


class Post(db.Model):
    __tablename__='posts'

    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.Text())
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    category=db.Column(db.String(255))
    posted_at=db.Column(db.DateTime, index=True, default=func.now())
    comments=db.relationship('Comment', backref='post', lazy='dynamic')

    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def get_pitches(self):
        pitches=Post.query.all()
        return pitches

    def get_pitch(self):
        pitch=Post.query.filter_by(id)
        return pitch

    def display_user(self):
        if Post.user_id == User.id:
            return User.username
    

@login_manager.user_loader
def load_user(username):
    return User.query.get(int(username))