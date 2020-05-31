from django.db import models

# Create your models here.
class User(models.Model):
    """
    class containing user objects
    """
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=140)
    password = models.CharField(max_length=100)