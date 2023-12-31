from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from accounts.models import Avatar

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email")
        
class UserUpdateForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")

class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ("imagen",)