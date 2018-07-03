from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from django.contrib.auth.decorators import login_required
from HereticFamily.AppCode import WeatherUndergroundAPI
from HereticFamily.AppCode.Objects import Weather

@login_required
def weather(request):
    """Renders the Weather page."""
    assert isinstance(request, HttpRequest)
    Curr_Weather = Weather.GetCurrentWeather()
    Fore_Weather = WeatherUndergroundAPI.GetWeatherForecast('ID', 'KIDA')
        
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
            'IconLocation': '/static/Images/weather/icons/white/',
            'WeatherDescription': Curr_Weather.weatherdescription,
            
            'Temp_High0': Fore_Weather.SimpleForecast0.Temp_High,
            'Temp_Low0': Fore_Weather.SimpleForecast0.Temp_Low,
            'Wind_Speed0': Fore_Weather.SimpleForecast0.Wind_Speed_Avg,
            'Wind_Dir0': Fore_Weather.SimpleForecast0.Wind_Direction_Avg,
            'Humidity0': Fore_Weather.SimpleForecast0.HumidityAVG,
            'Weather_Icon0': Fore_Weather.SimpleForecast0.Icon_URL,
            'IconName0': Fore_Weather.SimpleForecast0.Icon,
            'QPFAllDay0': Fore_Weather.SimpleForecast0.QPF_AllDay,
            
            'Temp_High1': Fore_Weather.SimpleForecast1.Temp_High,
            'Temp_Low1': Fore_Weather.SimpleForecast1.Temp_Low,
            'Wind_Speed1': Fore_Weather.SimpleForecast1.Wind_Speed_Avg,
            'Wind_Dir1': Fore_Weather.SimpleForecast1.Wind_Direction_Avg,
            'Humidity1': Fore_Weather.SimpleForecast1.HumidityAVG,
            'Weather_Icon1': Fore_Weather.SimpleForecast1.Icon_URL,
            'IconName1': Fore_Weather.SimpleForecast1.Icon,
            'QPFAllDay1': Fore_Weather.SimpleForecast1.QPF_AllDay,
            
            'Temp_High2': Fore_Weather.SimpleForecast2.Temp_High,
            'Temp_Low2': Fore_Weather.SimpleForecast2.Temp_Low,
            'Wind_Speed2': Fore_Weather.SimpleForecast2.Wind_Speed_Avg,
            'Wind_Dir2': Fore_Weather.SimpleForecast2.Wind_Direction_Avg,
            'Humidity2': Fore_Weather.SimpleForecast2.HumidityAVG,
            'Weather_Icon2': Fore_Weather.SimpleForecast2.Icon_URL,
            'IconName2': Fore_Weather.SimpleForecast2.Icon,
            'Date2': Fore_Weather.SimpleForecast2.Weekday,
            'QPFAllDay2': Fore_Weather.SimpleForecast2.QPF_AllDay,
            
            'Temp_High3': Fore_Weather.SimpleForecast3.Temp_High,
            'Temp_Low3': Fore_Weather.SimpleForecast3.Temp_Low,
            'Wind_Speed3': Fore_Weather.SimpleForecast3.Wind_Speed_Avg,
            'Wind_Dir3': Fore_Weather.SimpleForecast3.Wind_Direction_Avg,
            'Humidity3': Fore_Weather.SimpleForecast3.HumidityAVG,
            'Weather_Icon3': Fore_Weather.SimpleForecast3.Icon_URL,
            'IconName3': Fore_Weather.SimpleForecast3.Icon,
            'Date3': Fore_Weather.SimpleForecast3.Weekday,
            'QPFAllDay3': Fore_Weather.SimpleForecast3.QPF_AllDay,
            #'block1': '',
            #'block2': ,
        }
    return render(
        request,
        'weather.html',
        context
    )