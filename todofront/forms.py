from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Profile
from tasks.models import Task

class TaskForm(forms.ModelForm): 
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user']

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control validate text-white font-weight-bold pl-1',
            'id': 'login-username',
            }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control validate text-white font-weight-bold pl-1',
            'id': 'login-password',          
        }))

class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'id': 'reg-username',
            'class': 'form-control validate white-text font-weight-bold',
            'type': 'text',
        })
        self.fields['email'].widget.attrs.update({
            'id': 'reg-email',
        	'class': 'form-control validate white-text font-weight-bold',
            'type': 'email'
        	})
        self.fields['password1'].widget.attrs.update({
            'id': 'reg-password1',
        	'class': 'form-control validate white-text font-weight-bold',
            'type': 'password'
        	})
        self.fields['password2'].widget.attrs.update({
            'id': 'reg-password2',
        	'class': 'form-control validate white-text font-weight-bold',
            'type': 'password'
        	})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']