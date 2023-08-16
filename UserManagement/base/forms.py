from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post


# class UserCreationForm(forms.ModelForm):
#     username = forms.CharField(required = True)
#     email = forms.EmailField(required = True)
#     password1 = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]



class UserCreationForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required = True)
    class Meta:  
        model = User
        # fields = '__all__'
        fields = [ 'username','email', 'password1','password2']



class UserLogin(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget= forms.PasswordInput)
    
    class Meta: 
        # model = User
        fields = ['email', 'password']


class CreatePost(forms.ModelForm): 
    title = forms.CharField(required = True)
    # content = forms.CharField( max_length=500,required=True)

    class Meta: 
        model = Post
        # fields = ['title', 'content']
        fields = '__all__'