from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.home, name="home"),
    path('login', auth_views.LoginView.as_view(template_name = 'login.html',redirect_authenticated_user=True), name="login"),
    path('userlogin', views.login_user, name="login-user"),
    path('logout', views.logout_user, name="logout"),
]