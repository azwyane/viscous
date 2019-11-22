from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import post,profile, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    
    class Meta:
        model = post
        fields = ['title','text','images']

    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = [ 'username','email','password1','password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = [ 'username','email']



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']