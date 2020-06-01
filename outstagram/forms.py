from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Comment,Post


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class PostForm(forms.ModelForm):
    """
    class facilitates the creation of image form objects
    """
    class Meta:
        model = Post
        exclude = ['author', 'likes', 'pub_date']