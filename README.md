# weatherproject
 CS411 Weather Project (Alan, Michelle, Ryan)

# Team Members

    Alan
    Michelle
    Ryan

# Overview

This document provides detailed documentation of our Weather Web App project, a web-based application designed for the class CS411: Software Engineering at Boston University. Our application aims to provide real-time weather data for cities around the globe, along with providing a description of how that place "feels". We built this app with a simple yet informative user interface to ensure a seamless experience for users.

# Table of Contents

    Introduction
    Technologies Used
    Features
    API Endpoints
    Installation and Setup
    Testing
    Troubleshooting
    Future Developments
    License

# Introduction

The Weather Web App is a platform for users to quickly and easily check the current weather, forecasted weather for the upcoming days, and how it feels to be in that area at the moment. The app can serve a broad audience, including travelers, event planners, or simply individuals interested in knowing the weather conditions of a specific location in real time.

# Technologies Used

The web application was built using the following technologies:

    Front-end: HTML, CSS, JavaScript
    Back-end: Django Web framework (Python)
    Database: SQLite Database, generate with Django
    External API: VisualCrossing Weather API; IPGeolocation API
    Version Control: Git and GitHub

# Features
User Interface

A simple, easy-to-use interface is provided to navigate through the application. The UI comprises an input box for entering city names and a display panel for viewing the weather data.

# Current Weather

The main feature of the app is displaying real-time weather data for any city entered by the user. It includes temperature, humidity, wind speed, weather description, and an icon representing the weather conditions. The conditions will determine the output of the "how it feels like" section.

# Weather Forecast

The application can show a 7-day forecast for the selected city, detailing daily highs, lows, and weather conditions.

Favorite Cities / Past Cities - Not implemented as of 27 Jun.

Users can save their favorite cities to easily check the weather in those locations. Cities users have been to are also recorded.

# API Endpoints

The application uses the OpenWeatherMap API to fetch weather data.

    GET /api/weather/current/:city: Fetches current weather data for the provided city.
    GET /api/weather/forecast/:city: Fetches hourly/daily weather forecast for the provided city.
    GET /api/iplocation/ Fetches the ip address and gives the current city info

# Installation and Setup

To set up the application locally:

    Clone the repository: git clone https://github.com/CS411-weather-app/weather-app.git
    Navigate into the directory: cd weather-app
    Install dependencies: pip install -m requirements.txt
    Add a .env file at the root of your project and add the following lines:

    makefile

    VISUALCROSSING_API_KEY= 13895e54fdb14b1d98a233c3b7ac6814
    IPLOCATION_API_KEY=4WNC7AAWRUUG5JJZUDZKUMMKL

    Start the server: python manage.py runserver
    Open your browser and visit: http://localhost:8000

# Troubleshooting

If you encounter any issues while running the app, check the following:

    Ensure you have Django and required dependencies installed on your machine. 
    Verify that all dependencies were correctly installed. (Check the version on requirements.txt)
    Check if the .env file is correctly configured with valid credentials.
    Check for the correct API keys. 
    Do not enclose main folder file with others.

# Future Developments

For future versions, we are planning to add:

    User authentication to secure favorite cities.
    More detailed weather data, such as UV index, air quality, and sunrise/sunset times.
    Option to switch between metric and imperial units.

# License

This project is licensed under the MIT License. See the LICENSE file in the project root for more information.