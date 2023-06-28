from django.urls import path, include
from . import views
from .views import register_request, login_request
from .views import logout_request, index, profile

from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name="logout"),
    path("weather", index, name="weather"),
    path("profile", profile, name="profile"),
    path('accounts/', include('allauth.urls')),# all the stuff with accounts/
    path('logout-oauth', LogoutView.as_view()), #
    path('index', TemplateView.as_view(template_name="index.html"))
    # your other paths...
]
