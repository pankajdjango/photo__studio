from django.urls import path
from . import views

urlpatterns = [
    path('login.html/', views.signup_login, name='login'),
    path('logout/', views.logout, name='logout'),
]
