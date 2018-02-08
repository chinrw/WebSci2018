# Create your views here.
from pprint import pprint

from django.shortcuts import render

from lab2 import GetWeather_Data
from lab2.GetWeather_Data import CitySearchError


def index(request):
    return render(request, "lab2/lab2.html")


def weather(request):
    latitude = request.GET['latitude']
    longitude = request.GET['longitude']
    try:
        data = GetWeather_Data.from_lat_long(latitude, longitude)
        pprint(data)
    except CitySearchError as e:
        data = None
        print(e.message)

    return render(request, "lab2/weather.html", {'data': data})
