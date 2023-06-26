from django.shortcuts import render
import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm 
from .forms import NewUserForm 


from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



from . import forms

"""

# THIS IS FOR OPENWEATHER API

def index(request):
    url = 'http://api.openweathermap.org/data/3.0/weather?q={}&units=imperial&appid=16b49cdde47946d45a6ca4e7897e04e2'
    city = 'London'
    
    r = requests.get(url.format(city)).json()
    print(r)

    if r.get('main'):  # check if 'main' exists in the response
        city_weather = {
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
    else:
        city_weather = {}  # if 'main' does not exist, initialize an empty dict

    context = {'city_weather': city_weather}

    return render(request, 'weatherapp/weather.html', context)


# PRELIMINARY visualcrossing weather forcast.    
def index(request):
    url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key=4WNC7AAWRUUG5JJZUDZKUMMKL'
    city = 'London'

    r = requests.get(url.format(city=city)).json()

    if r.get('days'):
        city_weather = {
            'city': city,
            'temperature': r['days'][0]['temp'],
            'description': r['days'][0]['description'],
            'icon': r['days'][0]['icon'],
        }
    else:
        city_weather = {}

    context = {'city_weather': city_weather}

    return render(request, 'weatherapp/weather.html', context)

"""

def index(request):
    url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key=4WNC7AAWRUUG5JJZUDZKUMMKL'
    city = 'London'

    r = requests.get(url.format(city=city)).json()

    if r.get('days'):
        city_weather = {
            'city': city,
            'temperature': r['days'][0]['temp'],
            'description': r['days'][0]['description'],
            'windspeed': r['days'][0]['windspeed'],
            'winddir': r['days'][0]['winddir'],
            'humidity': r['days'][0]['humidity'],
            'precip': r['days'][0]['precip'],
            'precipprob': r['days'][0]['precipprob'],
            'visibility': r['days'][0]['visibility'],
            'cloudcover': r['days'][0]['cloudcover'],
            'dew': r['days'][0]['dew'],
            'sunrise': r['days'][0]['sunrise'],
            'sunset': r['days'][0]['sunset'],
        }
    else:
        city_weather = {}

    context = {'city_weather': city_weather}

    if request.user.is_authenticated:
        context['user'] = request.user

    return render(request, 'weatherapp/weather.html', context)

    #return render(request, 'weatherapp/weather.html', context)

"""

def register(request):
  if request.method == "POST":
    form = forms.UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      # cleaned data is a dictionary
      username = form.cleaned_data.get('username')
      messages.success(request, f"{username}, you're account is created, please login.")
      return redirect('user-login')
  else:
    form = forms.UserRegisterForm()
  return render(request, 'users/register.html', {'form': form})

@login_required()
def profile(request):
  return render(request, 'users/profile.html')

"""
# handles registering process. Ask to launch prompt.
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("weather.html")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    form = NewUserForm()
    return render(request=request, template_name="weatherapp/register.html", context={"register_form":form})

# handles login process.
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "weatherapp/login.html", {"login_form":form})


def logout_request(request):
    logout(request)
    return redirect("weather")  # or wherever you want to redirect after logout




@login_required
def profile(request):
    return render(request, 'weatherapp/weather.html')