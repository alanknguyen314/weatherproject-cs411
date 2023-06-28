from django.shortcuts import render
import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm 
from .forms import NewUserForm 
from django.db.models.functions.math import math


from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from datetime import datetime

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime('%Y-%m-%dT%H:%M:%S')

from . import forms


def calculate_feels_like(d_temperature, d_windspeed, d_humidity, d_uvindex): 
                        #or manybe make them ^ into a tuple to group better, your choice 
    
    feels_like = ''

    # Case 1 - Hot Day
    if d_temperature >= 75:

        if d_uvindex >= 7:
            feels_like += "High UV Index"
            if math.isclose(d_humidity, .40):
                # High UV and humidity
                feels_like += " and humidity may make temperatures feel warmer. "

            else:
                # Only High UV
                feels_like += "may make temperatures feel warmer. " 


        elif math.isclose(d_humidity, .40):
            # Only high humidity
            feels_like += "High humidity may make temperatures feel warmer. "

        
        if d_windspeed >= 7:
                feels_like += "Breeze may provide some relief against hot temperatures."
        
        elif not math.isclose(d_humidity, .40): 
            if d_uvindex < 7:
                feels_like = "Temperature reflects outside conditions."

    # Case 2 - Cold/normal day
    else: 

        if d_windspeed >= 7:
            feels_like += "Breeze may make temperatures feel slightly cooler. "

        elif d_windspeed >= 15:
            feels_like += "High wind speeds make may temperatures feel cooler. "

        else: 
            feels_like = "Temperature reflects outside conditions."

    return feels_like 

def index(request):
    #toNote: below is very jank code, but it work, I will clean it up later, you can also change whatever you want
    response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=13895e54fdb14b1d98a233c3b7ac6814").json()
    #print(response.status_code)
    #print(response.content)

    city_data = response #city_data is json file.
    api_key = '4WNC7AAWRUUG5JJZUDZKUMMKL'

    #url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key={api_key}}'
    url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{time}?unitGroup=us&key={api_key}'

    # Request hourly weather data
    #hourly_url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key={api_key}&include=hours'
    city = city_data["city"]
    #daily_response = requests.get(daily_url.format(city=city, api_key = api_key)).json()
    #hourly_response = requests.get(hourly_url.format(city=city, api_key = api_key)).json()
    #print("HERE IS DAILY:", daily_response)
    #print("HERE IS HOURLY:", hourly_response)
    r = requests.get(url.format(city=city, time = formatted_datetime,  api_key=api_key)).json()
    #print(r.get('hours'))
    print(url.format(city=city, time = formatted_datetime,  api_key=api_key))
    if r.get('days'):
        #hourly_data = hourly_response['hours'][0]
        d = r['days'][0]
        h = d['hours'][0]

        city_weather = {
            'city': city,
            'daily_temperature': d['temp'],
            'daily_max': d['tempmax'],
            'daily_min': d['tempmin'],
            'daily_description': d['description'],
            'daily_windspeed': d['windspeed'],
            'daily_winddir': d['winddir'],
            'daily_humidity': d['humidity'],
            'daily_precip': d['precip'],
            'daily_precipprob': r['days'][0]['precipprob'], #Ryann, please delete variables as you see fit
            'daily_visibility': r['days'][0]['visibility'], #these are just here becuase they might be useful
            'daily_cloudcover': r['days'][0]['cloudcover'], #same for the hourly ones, etc etc
            'daily_dew': r['days'][0]['dew'],
            'daily_uvindex': r['days'][0]['uvindex'],
            'daily_sunrise': r['days'][0]['sunrise'],
            'daily_sunset': r['days'][0]['sunset'],
            #this is here to show a clear split between daily and hourly values
            'hourly_temperature': d['hours'][0]['temp'],
            #'hourly_description': d['hours'][0]['description'],
            'hourly_windspeed': d['hours'][0]['windspeed'],
            'hourly_winddir': d['hours'][0]['winddir'],
            'hourly_humidity': d['hours'][0]['humidity'],
            'hourly_precip': d['hours'][0]['precip'],
            'hourly_precipprob': d['hours'][0]['precipprob'],
            'hourly_visibility': d['hours'][0]['visibility'],
            'hourly_cloudcover': h['cloudcover'],
            'hourly_dew': h['dew'],
            #'hourly_sunrise': h['sunrise'],
            #'hourly_sunset': h['sunset'],
        }

        feels_like = calculate_feels_like(r['days'][0]['temp'], r['days'][0]['windspeed'], r['days'][0]['humidity'], r['days'][0]['uvindex'])
    else:
        city_weather = {}
        feels_like = None

    context = {'city_weather': city_weather,
            'city_data': city_data,
            'feels_like': feels_like}

    if request.user.is_authenticated:
        context['user'] = request.user

    return render(request, 'weatherapp/weather.html', context)


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
    return render(request, 'weatherapp/profile.html')
