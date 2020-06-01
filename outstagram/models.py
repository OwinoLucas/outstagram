from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from PIL import Image

# Create your models here.
class Profile(models.Model):
    """
    class facilitates the creation of profile objects
    """
    bio = models.CharField(max_length=70)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default = 'default.jpg',upload_to='profiles/')
    def __str__(self):
        """
        function returns informal representations of the models' objects
        """
        return f'{self.user.username} Profile'

    def save_profile(self):
        """
        method saves entered profiles to the database
        """
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

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

    
#Image class kwa lms
class Post(models.Model):
    """
    class containing post objects
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True,upload_to='posts/')
    image_name = models.CharField(max_length=30, null=True)
    caption = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author.username} post'

    @classmethod
    def display_posts(cls):
        posts = cls.objects.all()
        return posts

    @classmethod
    def search_user_by_profile(cls,user_search):
        author_details = cls.objects.filter(profile__user__icontains=user_search)
        return author_details

    def save_post(self):
        """
        method saves added post object
        """
        super().save()

        img = Image.open(self.image.path)
        if img.height > 575 or img.width > 560:
            output_size = (575,560)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def update_post(self, using=None, fields=None, **kwargs):
        """
        method updates saved post
        """
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)

    def delete_post(self):
        """
        method deletes saved post object
        """
        self.delete()



class Comment(models.Model):
    """
    class containing comment objects
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=500, blank=False)

    def __str__(self):
        return self.body