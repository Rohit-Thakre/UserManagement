from django.shortcuts import render
from django.contrib.auth import login, logout , authenticate
from .forms import UserCreationForm

def home(request): 
    return render(request,'base/home.html')




def Ulogin(request): 
    pass



def sign_up(request):
    form = UserCreationForm()
    



    return render(request, 'base/sign_up.html', {'form': form})