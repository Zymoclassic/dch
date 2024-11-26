from django.urls import path
from . import views
from django.urls import reverse


urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),    
]

