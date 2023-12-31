from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('profile/<int:key>/', views.profile, name='profile'),

    
    path('login/', views.UserLogin, name = 'login'), 
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.sign_out, name='sign_out'),
    path('post/', views.post, name='post'), 
    path('update-post/<int:key>/', views.update_post, name='update-post'), 
    path('delete-post/<int:key>/', views.delete_post, name='delete-post'),

]