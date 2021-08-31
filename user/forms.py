from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'profilePic', 'introduce']

class CustomUserChangeForm(UserChangeForm):
    password = None        
    username = forms.CharField(label='아이디', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    profilePic = forms.ImageField(label='프로필사진', required=False)
    introduce = forms.CharField(label='자기소개', required=False, widget=forms.Textarea)

    class Meta:
        model = CustomUser
        fields = ['username', 'profilePic', 'introduce']