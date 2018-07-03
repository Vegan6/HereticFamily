#Check DB for interval weather
#If passed then pull from API, insert to DB, pull from DB
#Else pull from DB

import requests
import json
#import logging
#import os.path
from . import helper
from HereticFamily.AppCode.Objects import Weather
#http://api.wunderground.com/api/892a7ac61426b970/conditions/q/ID/Idaho_Falls.json
#Forecast: http://api.wunderground.com/api/892a7ac61426b970/forecast/q/ID/Idaho_Falls.json
#Zip Query: http://api.wunderground.com/api/892a7ac61426b970/conditions/q/ID/83404.json

def GetWeatherCurrent(State, City):
  # Also returns 3-day forecast
  url = "http://api.wunderground.com/api/%s/conditions/q/%s/%s.json" % (helper.WU_API_KEY, helper.WU_STATE, helper.WU_CITY)
  response = requests.get(url)
  response
  if response.status_code == 200:
      if response.text[0] and response.text[0] != 'REQUEST_TIMEOUT':
          return Weather.CurrentWeather(json.loads(response.text))
      else:
          raise Exception('Ooops Error:\n' + response.text)
  else:
      raise Exception('Error:\n' + response.text)
      
def GetWeatherForecast(State, City):
  # Also returns 3-day forecast
  url = "http://api.wunderground.com/api/%s/forecast/q/%s/%s.json" % (helper.WU_API_KEY, helper.WU_STATE, helper.WU_CITY)
  response = requests.get(url)
  response
  if response.status_code == 200:
      if response.text[0] and response.text[0] != 'REQUEST_TIMEOUT':
          return Weather.WeatherForecast(json.loads(response.text))
      else:
          raise Exception('Ooops Error:\n' + response.text)
  else:
      raise Exception('Error:\n' + response.text)
    
    