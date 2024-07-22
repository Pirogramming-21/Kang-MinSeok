# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Post


class SignupForm(UserCreationForm):
    username = forms.CharField(
        label="아이디", widget=forms.TextInput(attrs={"class": "signup-input"})
    )
    password1 = forms.CharField(
        label="비밀번호", widget=forms.PasswordInput(attrs={"class": "signup-input"})
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput(attrs={"class": "signup-input"}),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
        ]

class PostForm(forms.ModelForm):
    photo = forms.ImageField()
    content = forms.Textarea()
    
    class Meta:
        model = Post
        fields = [
            "photo",
            "content"
        ]