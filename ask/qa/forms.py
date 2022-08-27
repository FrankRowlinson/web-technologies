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
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        del self.fields['password1']
        del self.fields['password2']
        self.fields['username'].help_text = None
    
    def save(self, commit=True):
        self.cleaned_data['password1'] = self.cleaned_data['password']
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
