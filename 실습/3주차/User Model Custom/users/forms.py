from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class' : 'signup-input'
            }
        )
    )
    email = forms.CharField(
        label='이메일',
        widget=forms.TextInput(
            attrs={
                'class' : 'signup-input'
            }
        )
    )
    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class' : 'signup-input'
            }
        )
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class' : 'signup-input'
            }
        )
    )
    name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class' : 'signup-input'
            }
        )
    )
    nickname = forms.CharField(
        label='닉네임',
        widget=forms.TextInput(
            attrs={
                'class' : 'signup-input'
            }
        )
    )
    gender = forms.ChoiceField(
        label='성별',
        choices=[('', '--------')] + User.GENDER_CHOICE,
        widget=forms.Select(
            attrs={
                'class': 'signup-input'
            }
        )
    )
    job = forms.ChoiceField(
        label='직업',
        choices=[('', '--------')] + User.JOB_CHOICE,
        widget=forms.Select(
            attrs={
                'class': 'signup-input'
            }
        )
    )
    birth = forms.CharField(
        label='생일',
        widget=forms.TextInput(
            attrs={
                'class' : 'signup-input'
            }
        )
    )
    desc = forms.CharField(
        label='설명',
        widget=forms.TextInput(
            attrs={
                'class' : 'signup-input'
            }
        )
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'name', 'nickname', 'gender', 'job', 'birth', 'desc']