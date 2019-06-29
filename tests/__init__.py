import unittest
from app.models import Comment, User, Post
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password='peels')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('peels'))


class TestComment(unittest.TestCase):

    def setUp(self):
        self.user_James = User(
            username='James', password='peels', email='james@ms.com')
        self.new_comment = Comment(id=12345, post_id='2', user_id='2' pitch_comment='Eat food', user=self.user_James)

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id, 12345)
        self.assertEquals(self.new_comment.post_id, '2')
        self.assertEquals(self.new_comment.user_id, '2')
        self.assertEquals(self.new_comment.pitch_comment, 'Eat food')
        self.assertEquals(self.new_comment.user,
                          self.user_James, self.new_post)

    def test_save_comment(self):
        self.new_comment.save_comment()
        comments = Comment.query.all()
        self.assertTrue(len(comments) > 0)


class TestPost(unittest.TestCase):

    def setUp(self):
        self.user_James = User(
            username='James', password='peels', email='james@ms.com')
        self.new_post = Post(id=1234, text='meat', user_id=1,
                             category='food', user=self.user_James)

    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.id, 1234)
        self.assertEquals(self.new_post.user_id, 1)
        self.assertEquals(self.new_post.category, 'food')
       # self.assertEquals(self.new_post.comments,'t')
        self.assertEquals(self.new_post.user, self.user_James)

    def test_save_post(self):
        self.new_post.save_pitch()
        posts = Post.query.all()
        self.assertTrue(len(posts) > 0)


