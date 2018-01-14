from django import forms
from django.forms import ModelForm
from users.models import User

class LoginForm(forms.Form):
    login_username = forms.CharField(label='username')
    login_password = forms.CharField(widget=forms.PasswordInput(),label='password')

class NewUserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
