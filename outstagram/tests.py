from django.test import TestCase
from .models import User


# Create your tests here.
class UserTestClass(TestCase):
    """
    test class to test user objects
    """
    def setUp(self):
        self.lucas = User(username = 'Lucas',email = 'luca@gmail.com',password = 'qwerty')