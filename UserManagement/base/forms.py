from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class UserCreationForm(forms.ModelForm):
#     username = forms.CharField(required = True)
#     email = forms.EmailField(required = True)
#     password1 = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]



class UserCreationForm(UserCreationForm):
    class Meta:  
        model = User
        # fields = '__all__'
        fields = [ 'email', 'password1','password2']