from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.sign_up, name = 'login'), 
    path('sign_up/', views.sign_up, name='sign_up'),

]