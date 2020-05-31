from django.db import models
from  django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """
    class facilitates the creation of profile objects
    """
    bio = models.CharField(max_length=70)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profiles/')
    def __str__(self):
        """
        function returns informal representations of the models' objects
        """
        return self.user

    def save_profile(self):
        """
        method saves entered profiles to the database
        """
        self.save()

    def update_profile(self, using=None, fields=None, **kwargs):
        """
        method updates saved profile
        """
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)

    def delete_profile(self):
        """
        method deletes saved profile
        """
        self.delete()


class Post(models.Model):
    """
    class containing post objects
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts')
    caption = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author.username} post'


class Comment(models.Model):
    """
    class containing comment objects
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.Case)
    body = models.TextField(max_length=500, blank=False)

    def __str__(self):
        return self.body