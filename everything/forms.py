from django import forms
from .models import Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BlogPost
from .models import Blogger

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'content']

    author_name = forms.CharField(label='Your Name', max_length=100)
    content = forms.CharField(label='Comment', widget=forms.Textarea(attrs={'rows': 4}))

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=200 , required=True)
    password = forms.CharField(max_length=200 , required=True)
    # Add any additional fields or customization you need


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# forms.py

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']