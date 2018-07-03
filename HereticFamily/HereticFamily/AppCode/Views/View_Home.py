from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from django.contrib.auth.decorators import login_required
from HereticFamily.AppCode.Objects import Weather

@login_required
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    #Curr_Weather = WeatherUndergroundAPI.GetWeatherCurrent('ID', 'KIDA')
    Curr_Weather = Weather.GetCurrentWeather()
        
    context = {
            'title': 'Heretic Family',
            'Year': datetime.now().year,
            'Temp_String': Curr_Weather.temperature,
            'FeelsLike': Curr_Weather.feelslike,
            'Weather_Icon': Curr_Weather.iconurl,
            'IconName': Curr_Weather.iconname,
            'ObservationLocation_Full': Curr_Weather.stationid.observationlocationfull,
            'Feels_Like': Curr_Weather.feelslike,
            'Wind_Speed': Curr_Weather.windspeed,
            'Wind_Dir': Curr_Weather.winddirection,
            'Humidity': "{0:.0f}%".format(Curr_Weather.relativehumidity * 100),
            
            
        }
    return render(
        request,
        'index.html',
        context
    )