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