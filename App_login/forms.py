from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields
from App_login. models import User_profile


class SignUpForm(UserCreationForm):
    email=forms.EmailField(label="Enter Your Email",required=True)
    class Meta:
        model=User
        fields=('username','email','password1','password2')

class ProfileChange(UserChangeForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','password')



class ProfilePic(forms.ModelForm):
    class Meta:
        model=User_profile
        fields=('profile_pic',)