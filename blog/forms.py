from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment


class CustomUserCreationForm(UserCreationForm):
    """
    User registration form extending Django's UserCreationForm with email field.
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CommentForm(forms.ModelForm):
    """
    Form for submitting or editing a comment on a blog post.
    """
    class Meta:
        model = Comment
        fields = ('body',)        
