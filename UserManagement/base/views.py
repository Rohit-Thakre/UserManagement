from django.shortcuts import render, redirect
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import UserCreationForm, CreatePost
from django.contrib.auth.models import User
from .models import Post

def home(request): 
    # posts = Post.objects.all()
    q= request.GET.get('q') 
    q = request.GET.get('q') if q else ""
    posts = Post.objects.filter(
        Q(creator__username__icontains=q)| 
        Q(title__icontains=q) | 
        Q(content__icontains=q)
        )
    context = {'posts': posts}
    return render(request,'base/home.html' ,context)




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


@login_required(login_url = 'login')
def post(request): 

    form = CreatePost()

    if request.method == "POST": 
        form = CreatePost(request.POST)

        if form.is_valid(): 
          
            form.save(commit = False)
            form.creator = request.user
            post = form.save(commit=False)
            post.creator = request.user
            post.save()
            return redirect('home')
    
    return render(request, 'base/post.html', {"form": form})



def update_post(request, key): 
    data = Post.objects.get(id=key)
    form = CreatePost(instance= data)

    if request.method == 'POST': 
        form = CreatePost(request.POST, instance = data)
        form.save()
        return redirect('home')


    context = {'form':form}
    return render(request, 'base/post.html', context)




def delete_post(request, key): 
    post = Post.objects.get(id=key)
    

    if request.method == "POST":
        post.delete()
        print('post deleted ')
        return redirect('home')
    return render(request, 'base/delete.html', {'post': post})