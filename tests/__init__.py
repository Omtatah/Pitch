import unittest
from flask_login import current_user
from app.models import Comment, User, Post
from app import db


class PitchTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(
            username='james', password='12', email='james@mail.com')
        self.new_pitch = Pitch(id=123, pitch_content='Pitch content',
                               pitch_category='pickup', user=self.new_user)

    def tearDown(self):
        User.query.delete()
        Pitch.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_content, "Pitch content")
        self.assertEquals(self.new_pitch.pitch_category, 'pickup')
        self.assertEquals(self.new_pitch.user, self.new_user)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all()) > 0)


class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password='password')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('password'))


class TestPitch(unittest.TestCase):

    def setUp(self):
        self.user_james = User(
            username='james', password='12', email='james@mail.com')
        self.new_pitch = Pitch(pitch_content="Pitch Test",
                               pitch_category='Technology', user=self.user_james)
        self.new_comment = Comment(
            comment_content="Comment Test", pitch=self.new_pitch, user=self.user_james)

    def tearDown(self):
        db.session.delete(self)
        User.query.commit()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment_content, "Comment Test")
        self.assertEquals(self.new_comment.pitch, self.new_pitch)
        self.assertEquals(self.new_comment.user, self.user_james)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)
