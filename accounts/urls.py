from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import register_view, login_view, logout_view

urlpatterns = [
    path('accounts/login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name="register"),
]
