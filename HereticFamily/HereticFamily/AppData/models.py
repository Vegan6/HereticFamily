# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django_mysql.models import Bit1BooleanField

class DimWeatherstation(models.Model):
    stationid = models.CharField(db_column='StationID', primary_key=True, max_length=64)  
    displaylocationfull = models.CharField(db_column='DisplayLocationFull', max_length=256, blank=True, null=True)  
    displaylocationcity = models.CharField(db_column='DisplayLocationCity', max_length=128, blank=True, null=True)  
    displaylocationstate = models.CharField(db_column='DisplayLocationState', max_length=16, blank=True, null=True)  
    displaylocationstatename = models.CharField(db_column='DisplayLocationStateName', max_length=64, blank=True, null=True)  
    displaylocationcountry = models.CharField(db_column='DisplayLocationCountry', max_length=16, blank=True, null=True)  
    displaylocationzip = models.CharField(db_column='DisplayLocationZip', max_length=32, blank=True, null=True)  
    displaylocationlatitude = models.DecimalField(db_column='DisplayLocationLatitude', max_digits=10, decimal_places=8, blank=True, null=True)  
    displaylocationlongitude = models.DecimalField(db_column='DisplayLocationLongitude', max_digits=11, decimal_places=8, blank=True, null=True)  
    displaylocationelevation = models.DecimalField(db_column='DisplayLocationElevation', max_digits=6, decimal_places=1, blank=True, null=True)  
    observationlocationfull = models.CharField(db_column='ObservationLocationFull', max_length=256, blank=True, null=True)  
    observationlocationcity = models.CharField(db_column='ObservationLocationCity', max_length=128, blank=True, null=True)  
    observationlocationstate = models.CharField(db_column='ObservationLocationState', max_length=64, blank=True, null=True)  
    observationlocationcountry = models.CharField(db_column='ObservationLocationCountry', max_length=16, blank=True, null=True)  
    observationlocationlatitude = models.DecimalField(db_column='ObservationLocationLatitude', max_digits=10, decimal_places=8, blank=True, null=True)  
    observationlocationlongitude = models.DecimalField(db_column='ObservationLocationLongitude', max_digits=11, decimal_places=8, blank=True, null=True)  
    observationlocationelevation = models.DecimalField(db_column='ObservationLocationElevation', max_digits=6, decimal_places=1, blank=True, null=True)  
    localtimezoneshort = models.CharField(db_column='LocalTimeZoneShort', max_length=16, blank=True, null=True)  
    localtimezonelong = models.CharField(db_column='LocalTimeZoneLong', max_length=64, blank=True, null=True)  
    localtimezoneoffset = models.CharField(db_column='LocalTimeZoneOffset', max_length=16, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Dim_WeatherStation'


class FactTasklist(models.Model):
    taskid = models.AutoField(db_column='TaskID', primary_key=True)
    taskname = models.CharField(db_column='TaskName', max_length=128)
    taskdesc = models.CharField(db_column='TaskDesc', max_length=2048, blank=True, null=True)
    taskcreateddate = models.DateField(db_column='TaskCreatedDate', blank=True, null=False)
    completed = Bit1BooleanField(db_column='Completed')
    completiondate = models.DateField(db_column='CompletionDate', blank=True, null=True)
    createdby = models.ForeignKey('AuthUser', db_column='CreatedBy', related_name='task_createdby')
    assignedto = models.ForeignKey('AuthUser', db_column='AssignedTo', blank=True, null=True, related_name='task_assignedto')

    class Meta:
        managed = False
        db_table = 'Fact_TaskList'


class FactWeathercurrent(models.Model):
    stationid = models.ForeignKey(DimWeatherstation, models.DO_NOTHING, db_column='StationID', primary_key=True)
    observationtimefriendly = models.CharField(db_column='ObservationTimeFriendly', max_length=256, blank=True, null=True)
    observationdatetime = models.DateTimeField(db_column='ObservationDateTime', blank=True, null=True)
    weatherdescription = models.CharField(db_column='WeatherDescription', max_length=64, blank=True, null=True)
    temperature = models.DecimalField(db_column='Temperature', max_digits=6, decimal_places=2, blank=True, null=True)
    relativehumidity = models.DecimalField(db_column='RelativeHumidity', max_digits=3, decimal_places=2, blank=True, null=True)
    windstring = models.CharField(db_column='WindString', max_length=32, blank=True, null=True)
    winddirection = models.CharField(db_column='WindDirection', max_length=16, blank=True, null=True)
    winddegrees = models.SmallIntegerField(db_column='WindDegrees', blank=True, null=True)
    windspeed = models.SmallIntegerField(db_column='WindSpeed', blank=True, null=True)
    windgustspeed = models.SmallIntegerField(db_column='WindGustSpeed', blank=True, null=True)
    pressuremb = models.IntegerField(db_column='PressureMB', blank=True, null=True)
    pressurein = models.DecimalField(db_column='PressureIN', max_digits=6, decimal_places=2, blank=True, null=True)
    dewpoint = models.SmallIntegerField(db_column='Dewpoint', blank=True, null=True)
    windchill = models.SmallIntegerField(db_column='WindChill', blank=True, null=True)
    feelslike = models.SmallIntegerField(db_column='FeelsLike', blank=True, null=True)
    visibilitymiles = models.DecimalField(db_column='VisibilityMiles', max_digits=10, decimal_places=2, blank=True, null=True)
    precipitationonehourin = models.DecimalField(db_column='PrecipitationOneHourIN', max_digits=10, decimal_places=2, blank=True, null=True)
    precipitationdayin = models.DecimalField(db_column='PrecipitationDayIN', max_digits=10, decimal_places=2, blank=True, null=True)
    iconname = models.CharField(db_column='IconName', max_length=32, blank=True, null=True)
    iconurl = models.CharField(db_column='IconURL', max_length=1024, blank=True, null=True)
    updatedatetime = models.DateTimeField(db_column='UpdateDateTime')

    class Meta:
        managed = False
        db_table = 'Fact_WeatherCurrent'
        unique_together = (('stationid', 'updatedatetime'),)
        
class FactWeatherforecasttext(models.Model):
    stationid = models.ForeignKey(DimWeatherstation, models.DO_NOTHING, db_column='StationID')  
    forecasttextperiodnumber = models.IntegerField(db_column='ForecastTextPeriodNumber', primary_key=True)  
    forecasttextperioddesc = models.CharField(db_column='ForecastTextPeriodDesc', max_length=64, blank=True, null=True)  
    observationtimefriendly = models.CharField(db_column='ObservationTimeFriendly', max_length=256, blank=True, null=True)  
    observationdatetime = models.DateTimeField(db_column='ObservationDateTime', blank=True, null=True)  
    weatherdescription = models.CharField(db_column='WeatherDescription', max_length=2048, blank=True, null=True)  
    iconname = models.CharField(db_column='IconName', max_length=32, blank=True, null=True)  
    updatedatetime = models.DateTimeField(db_column='UpdateDateTime')  

    class Meta:
        managed = False
        db_table = 'Fact_WeatherForecastText'
        unique_together = (('forecasttextperiodnumber', 'stationid', 'updatedatetime'),)

class FactWeatherforecastsimple(models.Model):
    stationid = models.ForeignKey(DimWeatherstation, models.DO_NOTHING, db_column='StationID')  
    forecastsimpledaynumber = models.IntegerField(db_column='ForecastSimpleDayNumber', primary_key=True)  
    observationtimefriendly = models.CharField(db_column='ObservationTimeFriendly', max_length=256, blank=True, null=True)  
    observationdatetime = models.DateTimeField(db_column='ObservationDateTime', blank=True, null=True)  
    weatherdescription = models.CharField(db_column='WeatherDescription', max_length=64, blank=True, null=True)  
    temperaturehigh = models.DecimalField(db_column='TemperatureHigh', max_digits=6, decimal_places=2, blank=True, null=True)  
    temperaturelow = models.DecimalField(db_column='TemperatureLow', max_digits=6, decimal_places=2, blank=True, null=True)  
    relativehumidity = models.DecimalField(db_column='RelativeHumidity', max_digits=3, decimal_places=2, blank=True, null=True)  
    winddirectionmax = models.CharField(db_column='WindDirectionMax', max_length=16, blank=True, null=True)  
    winddirectionavg = models.CharField(db_column='WindDirectionAvg', max_length=16, blank=True, null=True)  
    winddegreeshigh = models.SmallIntegerField(db_column='WindDegreesHigh', blank=True, null=True)  
    winddegreesavg = models.SmallIntegerField(db_column='WindDegreesAvg', blank=True, null=True)  
    windspeedhigh = models.SmallIntegerField(db_column='WindSpeedHigh', blank=True, null=True)  
    windspeedavg = models.SmallIntegerField(db_column='WindSpeedAvg', blank=True, null=True)  
    qpfallday = models.DecimalField(db_column='QPFAllDay', max_digits=6, decimal_places=2, blank=True, null=True)  
    qpfday = models.DecimalField(db_column='QPFDay', max_digits=6, decimal_places=2, blank=True, null=True)  
    qpfnight = models.DecimalField(db_column='QPFNight', max_digits=6, decimal_places=2, blank=True, null=True)  
    snowallday = models.DecimalField(db_column='SnowAllDay', max_digits=6, decimal_places=2, blank=True, null=True)  
    snowday = models.DecimalField(db_column='SnowDay', max_digits=6, decimal_places=2, blank=True, null=True)  
    snownight = models.DecimalField(db_column='SnowNight', max_digits=6, decimal_places=2, blank=True, null=True)  
    iconname = models.CharField(db_column='IconName', max_length=32, blank=True, null=True)  
    updatedatetime = models.DateTimeField(db_column='UpdateDateTime')  

    class Meta:
        managed = False
        db_table = 'Fact_WeatherForecastSimple'
        unique_together = (('forecastsimpledaynumber', 'stationid', 'updatedatetime'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    
    def __str__(self):
      return '%s (%s %s)' % (self.username, self.first_name, self.last_name)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
