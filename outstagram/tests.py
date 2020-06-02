from django.test import TestCase
from .models import Profile, Post
from django.contrib.auth.models import User

# Create your tests here.
class  ProfileModelTests(TestCase):
    """
    class facilitates the creation of test units to test profile model's behavior
    """
    def setUp(self):
        """
        method defines the instructions to be executed before each test
        """
        self.new_user = User(username="wendo", email="wendo11@gmail.com", password="qwerty")
        self.new_user.save()
        self.new_profile = Profile(bio="anything crazy", user=self.new_user, profile_pic="mypic.jpg")
    
    def test_instance(self):
        """
        method checks model's object are initialization
        """
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_profile(self):
        """
        test unit tests if the model's object are saved to the database
        """
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    
    def test_update_profile(self):
        """
        method  update profile function
        """
        self.new_profile.save_profile()
        Profile.objects.filter(pk=self.new_profile.pk).update(bio="update smthg")
        self.new_profile.update_profile()
        self.assertEqual(self.new_profile.bio, 'update smthg')
    
    def test_delete_profile(self):
        """
        method  delete function
        """
        self.new_profile.save_profile()
        Profile.objects.filter(pk=self.new_profile.pk).delete()
        self.new_profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

class PostModelTests(TestCase):
    """
    class facilitates the creation of tests to test model's behavior
    """
    def setUp(self):
        """
        method dictates the instructions to be executed before each test
        """
        self.new_user = User(username="wendo", email="wendo@gmail.com", password="password")
        self.new_user.save()
        self.new_profile = Profile(bio="something ", user=self.new_user, profile_pic="default.jpg")
        self.new_profile.save()
        self.image = Post(image='default.jpg', image_name='default', caption='random pic', author=self.new_pauthor, likes=0, comments='random comment')
    
    def test_instance(self):
        """
        method checks if objects are initialized properly
        """
        self.assertTrue(isinstance(self.image, Post))
    
    def test_save_post(self):
        """
        method tests if an added post objects is saved to the database
        """
        self.image.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)
    
    def test_update_post(self):
        """
        method test if a saved post object can be updated
        """
        self.image.save_post()
        Post.objects.filter(pk=self.image.pk).update(image_name="random")
        self.image.update_post()
        self.assertEqual(self.image.image_name, 'random')

    def test_delete_post(self):
        """
        method check if a saved post objects can be deleted
        """
        self.image.save_post()
        Post.objects.filter(pk=self.image.pk).delete()
        self.image.delete_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) == 0)
        
class CommentModelTests(TestCase):
    """
    class facilitates the creation of tests to test comments' model behavior
    """
    def setUp(self):
        """
        method defines the instructions to be executed before each test
        """
        self.new_user = User(username="wendo", email="wendo@gmail.com", password="password")
        self.new_user.save()
        self.new_profile = Profile(bio="something ", user=self.new_user, profile_pic="default.jpg")
        self.new_profile.save()
        self.image = Post(image='default.jpg', image_name='default', caption='random pic', author=self.new_pauthor, likes=0, comments='random comment')
        self.image.save()
        self.new_comment=Comment(user=self.new_user, image=self.image, comment='some comment')
    
    def test_instance(self):
        """
        method checks if an object is initialized properly
        """
        self.assertTrue(isinstance(self.new_comment, Comment))
    
    def test_save_comment(self):
        """
        method checks if added comment is saved to the database
        """
        self.new_comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)
    
    def test_delete_comment(self):
        """
        method checks if savd comment can be deleted
        """
        self.new_comment.save_comment()
        self.new_comment.delete_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) == 0)
    
    def test_get_comments(self):
        """
        method checks if it is possible to get all saved comments
        """
        self.new_comment.save_comment()
        comments = Comment.get_comments(self.image.id)
        self.assertTrue(len(comments) == 1)