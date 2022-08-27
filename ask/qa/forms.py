from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *

class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'title',
            'text',
        ]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'text',
            'question',
        ]


class UserSignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None