from django.contrib.auth import get_user_model
from django import forms

user = get_user_model()


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = user
        fields = ['username', 'email', 'password']
