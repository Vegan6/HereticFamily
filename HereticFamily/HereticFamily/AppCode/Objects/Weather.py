import logging
from HereticFamily.AppData import models
from HereticFamily.AppCode import WeatherUndergroundAPI
from HereticFamily.AppCode import helper
from datetime import datetime, timedelta

def GetCurrentWeather():
  # Check DB for values updated in the last hour
  # Pull if exists, else use api to update and return
    if not models.FactWeathercurrent.objects.filter(stationid=helper.WU_StationID).exists():
        CurrentWeather = WeatherUndergroundAPI.GetWeatherCurrent(helper.WU_STATE, helper.WU_CITY)
        StationID = models.DimWeatherstation.objects.get(stationid = CurrentWeather.Station_ID)
        
        Curr_Weather = models.FactWeathercurrent(          
            stationid=StationID,
            observationtimefriendly=CurrentWeather.ObservationTime_Friendly,
            observationdatetime=helper.GetUpdateTime(CurrentWeather.ObservationEPOCH),
            weatherdescription=CurrentWeather.Weather_Friendly,
            temperature=CurrentWeather.Temperature,
            relativehumidity=CurrentWeather.Humidity,
            windstring=CurrentWeather.Wind_String,
            winddirection=CurrentWeather.Wind_Direction,
            winddegrees=CurrentWeather.Wind_Degrees,
            windspeed=CurrentWeather.Wind_Speed,
            windgustspeed=CurrentWeather.Wind_Speed_Gust,
            pressuremb=CurrentWeather.Pressure_MB,
            pressurein=CurrentWeather.Pressure,
            dewpoint=CurrentWeather.DewPoint,
            windchill=CurrentWeather.WindChill,
            feelslike=CurrentWeather.FeelsLike,
            visibilitymiles=CurrentWeather.Visibility,
            precipitationonehourin=CurrentWeather.PrecipitationHour,
            precipitationdayin=CurrentWeather.PrecipitationDay,
            iconname=CurrentWeather.Icon,
            iconurl=CurrentWeather.Icon_URL,
            updatedatetime=datetime.now()
            )
        Curr_Weather.save()
    # If In DB async call to API (if update time > threshold) and return DB
    else:
        Curr_Weather = models.FactWeathercurrent.objects.get(stationid=helper.WU_StationID)
        if Curr_Weather.updatedatetime <= datetime.now() - timedelta(hours=1):
            CurrentWeather = WeatherUndergroundAPI.GetWeatherCurrent(helper.WU_STATE, helper.WU_CITY)
            StationID = models.DimWeatherstation.objects.get(stationid = CurrentWeather.Station_ID)
                   
            Curr_Weather.stationid=StationID
            Curr_Weather.observationtimefriendly=CurrentWeather.ObservationTime_Friendly
            Curr_Weather.observationdatetime=helper.GetUpdateTime(CurrentWeather.ObservationEPOCH)
            Curr_Weather.weatherdescription=CurrentWeather.Weather_Friendly
            Curr_Weather.temperature=CurrentWeather.Temperature
            Curr_Weather.relativehumidity=CurrentWeather.Humidity
            Curr_Weather.windstring=CurrentWeather.Wind_String
            Curr_Weather.winddirection=CurrentWeather.Wind_Direction
            Curr_Weather.winddegrees=CurrentWeather.Wind_Degrees
            Curr_Weather.windspeed=CurrentWeather.Wind_Speed
            Curr_Weather.windgustspeed=CurrentWeather.Wind_Speed_Gust
            Curr_Weather.pressuremb=CurrentWeather.Pressure_MB
            Curr_Weather.pressurein=CurrentWeather.Pressure
            Curr_Weather.dewpoint=CurrentWeather.DewPoint
            Curr_Weather.windchill=CurrentWeather.WindChill
            Curr_Weather.feelslike=CurrentWeather.FeelsLike
            Curr_Weather.visibilitymiles=CurrentWeather.Visibility
            Curr_Weather.precipitationonehourin=CurrentWeather.PrecipitationHour
            Curr_Weather.precipitationdayin=CurrentWeather.PrecipitationDay
            Curr_Weather.iconname=CurrentWeather.Icon
            Curr_Weather.iconurl=CurrentWeather.Icon_URL
            Curr_Weather.updatedatetime=datetime.now()
            Curr_Weather.save()
    return Curr_Weather
  
class CurrentWeather(dict):
    # Pull out different forecast options
    def Current_Observation(self):
      return self['current_observation']
      
    # Current Observation items
    @property
    def DewPoint(self):
      return self.Current_Observation()['dewpoint_f']

    @property
    def DewPoint_String(self):
      return self.Current_Observation()['dewpoint_string']

    @property
    def FeelsLike(self):
      return self.Current_Observation()['feelslike_f']

    @property
    def FeelsLike_String(self):
      return self.Current_Observation()['feelslike_string']

    @property
    def Icon(self):
      return self.Current_Observation()['icon']

    @property
    def Icon_URL(self):
      return self.Current_Observation()['icon_url'].replace('/i/c/k', '/i/c/i')

    @property
    def Humidity(self):
      humidityString = self.Current_Observation()['relative_humidity']
      humidityString = humidityString.strip('%')
      humidityDec = float(humidityString) / 100.0
      return humidityDec

    @property
    def ObservationTime_Friendly(self):
      return self.Current_Observation()['observation_time']
    
    @property
    def ObservationEPOCH(self):
      return int(self.Current_Observation()['observation_epoch'])
      
    @property
    def PrecipitationHour(self):
      return self.Current_Observation()['precip_1hr_in']
    
    @property
    def PrecipitationDay(self):
      return self.Current_Observation()['precip_today_in']

    @property
    def Pressure(self):
      return self.Current_Observation()['pressure_in']
      
    @property
    def Pressure_MB(self):
      return self.Current_Observation()['pressure_mb']

    @property
    def Station_ID(self):
      return self.Current_Observation()['station_id']

    @property
    def Temperature(self):
      return self.Current_Observation()['temp_f']

    @property
    def Visibility(self):
      return self.Current_Observation()['visibility_mi']

    @property
    def Weather_Friendly(self):
      return self.Current_Observation()['weather']

    @property
    def WindChill(self):
      return self.Current_Observation()['windchill_f']

    @property
    def WindChill_String(self):
      return self.Current_Observation()['windchill_string']
      
    @property
    def Wind_Degrees(self):
      return self.Current_Observation()['wind_degrees']

    @property
    def Wind_Direction(self):
      return self.Current_Observation()['wind_dir']

    @property
    def Wind_Speed(self):
      return self.Current_Observation()['wind_mph']

    @property
    def Wind_Speed_Gust(self):
      return self.Current_Observation()['wind_gust_mph']

    @property
    def Wind_String(self):
      return self.Current_Observation()['wind_string']

    def log(self, text):
      logging.basicConfig(filename = "py_log.txt", level = logging.ERROR)
      logging.info("!!!Problem:" + text)

class WeatherForecast(dict):
  #Gather simple forecast data
  def SimpleForecast(self):
    forecast = self['forecast']
    simpleforecast = forecast['simpleforecast']
    return simpleforecast['forecastday']

  # Region SimpleForecast
  @property
  def SimpleForecast0(self):
    return WeatherSimpleForecast(self.SimpleForecast()[0])
  
  @property
  def SimpleForecast1(self):
    return WeatherSimpleForecast(self.SimpleForecast()[1])
  
  @property
  def SimpleForecast2(self):
    return WeatherSimpleForecast(self.SimpleForecast()[2])
  
  @property
  def SimpleForecast3(self):
    return WeatherSimpleForecast(self.SimpleForecast()[3])
  # EndRegion
  
  def TextForecast(self):
    forecast = self['forecast']
    txtForecast = forecast['txt_forecast']
    return txtForecast['forecastday']
  
  @property
  def TextForecast0(self):
    return self.TextForecast()[0]
  
  @property
  def TextForecast1(self):
    return self.TextForecast()[1]
  
  @property
  def TextForecast2(self):
    return self.TextForecast()[2]
  
  @property
  def TextForecast3(self):
    return self.TextForecast()[3]
  
  @property
  def TextForecast4(self):
    return self.TextForecast()[4]
  
  @property
  def TextForecast5(self):
    return self.TextForecast()[5]
  
  @property
  def TextForecast6(self):
    return self.TextForecast()[6]
  
  @property
  def TextForecast7(self):
    return self.TextForecast()[7]

class WeatherSimpleForecast(dict):
    # Get Simple Forecast Objects
    def DateObject(self):
        return self['date']

    @property
    def Day_Pretty(self):
        return self.DateObject()['pretty']

    @property
    def DayNumber(self):
        return self.DateObject()['day']

    @property
    def Icon(self):
        return self['icon']

    @property
    def Icon_URL(self):
        return self['icon_url'].replace('/i/c/k', '/i/c/i')

    @property
    def HumidityAVG(self):
        return self['avehumidity']

    @property
    def HumidityMAX(self):
        return self['maxhumidity']

    @property
    def MonthName(self):
        return self.DateObject()['monthname']

    @property
    def MonthNameShort(self):
        return self.DateObject()['monthname_short']

    @property
    def MonthNumber(self):
        return self.DateObject()['month']
      
    @property
    def QPF_AllDay(self):
      qpfallday = self['qpf_allday']
      return qpfallday['in']
    
    @property
    def Snow_AllDay(self):
      snowallday = self['snow_allday']
      return snowallday['in']

    @property
    def Temp_High(self):
        high = self['high']
        return high['fahrenheit']

    @property
    def Temp_Low(self):
        low = self['low']
        return low['fahrenheit']

    @property
    def Weekday(self):
        return self.DateObject()['weekday']

    @property
    def WeekdayShort(self):
        return self.DateObject()['weekday_short']

    @property
    def Wind_Direction_Avg(self):
        avgWind = self['avewind']
        return avgWind['dir']

    @property
    def Wind_Direction_Max(self):
        maxWind = self['maxwind']
        return maxWind['dir']

    @property
    def Wind_Speed_Avg(self):
        avgWind = self['avewind']
        return avgWind['mph']

    @property
    def Wind_Speed_Max(self):
        maxWind = self['maxwind']
        return maxWind['mph']

    @property
    def Year(self):
        return self.DateObject()['year']

    def log(self, text):
        logging.basicConfig(filename = "py_log.txt", level = logging.ERROR)
        logging.info("!!!Problem:" + text)
