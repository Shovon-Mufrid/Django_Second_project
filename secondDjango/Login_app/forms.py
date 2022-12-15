from django import forms
from django.contrib.auth.models import User
from Login_app.models import UserInfo


#  form for built in model USER
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput()) #custom pass chng
    class Meta:
        model = User
        fields = ('username',  'password', 'email')

#  form for built in model UserInfo
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('fb_id', 'profile_pic')