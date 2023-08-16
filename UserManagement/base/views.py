from django.shortcuts import render, redirect
from django.contrib.auth import login, logout , authenticate
from .forms import UserCreationForm
from django.contrib.auth.models import User


def home(request): 
    return render(request,'base/home.html')




# def UserLogin(request):
#     if request.method == 'POST': 
#         email = request.POST['email']
#         pas = request.POST['pas']
#         # print(email, pas)

#         user_obj = User.objects.filter(email = email)
#         # print(user_obj)
#         if user_obj: 
#             user = authenticate(request, email = email,password = pas) 
#             print('error')
#             login(request, user)
#             return redirect('home')


#     return render(request, 'base/login.html')

def UserLogin(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            # messages.error(request, 'User not found.')
            return redirect('login')
       
        user = authenticate(username=username, password=password)
        if user is None:
            # messages.error(request, 'Wrong password.')
            return redirect('login')

        login(request, user)
        # return HttpResponse('logged in as : {}'.format(request.user))
        return redirect('home')

    return render(request, 'base/login.html')







def sign_up(request):
    form = UserCreationForm()

    if request.method == 'POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            login(request, user)
            return redirect('home')
    



    return render(request, 'base/sign_up.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('home')