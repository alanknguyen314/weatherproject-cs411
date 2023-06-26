from django.urls import path
from . import views
from .views import register_request, login_request
from .views import logout_request, index, profile


urlpatterns = [
    path('', views.index),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name="logout"),
    path("weather", index, name="weather"),
    path("profile", profile, name="profile"),
    # your other paths...
]
