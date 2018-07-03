# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(primary_key=True, max_length=40, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FactTasklist',
            fields=[
                ('taskid', models.AutoField(primary_key=True, serialize=False, db_column='TaskID')),
                ('taskname', models.CharField(max_length=128, db_column='TaskName')),
                ('taskdesc', models.CharField(max_length=2048, blank=True, null=True, db_column='TaskDesc')),
                ('taskcreatedate', models.DateField(blank=True, null=True, db_column='TaskCreateDate')),
                ('completed', models.BooleanField(db_column='Completed')),
                ('createdby', models.IntegerField(db_column='CreatedBy')),
                ('assignedto', models.IntegerField(blank=True, null=True, db_column='AssignedTo')),
            ],
            options={
                'db_table': 'Fact_TaskList',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FactWeathercurrent',
            fields=[
                ('displaylocationfull', models.CharField(max_length=256, blank=True, null=True, db_column='DisplayLocationFull')),
                ('displaylocationcity', models.CharField(max_length=128, blank=True, null=True, db_column='DisplayLocationCity')),
                ('displaylocationstate', models.CharField(max_length=16, blank=True, null=True, db_column='DisplayLocationState')),
                ('displaylocationstatename', models.CharField(max_length=64, blank=True, null=True, db_column='DisplayLocationStateName')),
                ('displaylocationcountry', models.CharField(max_length=16, blank=True, null=True, db_column='DisplayLocationCountry')),
                ('displaylocationzip', models.CharField(max_length=32, blank=True, null=True, db_column='DisplayLocationZip')),
                ('observationlocationfull', models.CharField(max_length=256, blank=True, null=True, db_column='ObservationLocationFull')),
                ('observationlocationcity', models.CharField(max_length=128, blank=True, null=True, db_column='ObservationLocationCity')),
                ('observationlocationstate', models.CharField(max_length=64, blank=True, null=True, db_column='ObservationLocationState')),
                ('observationlocationcountry', models.CharField(max_length=16, blank=True, null=True, db_column='ObservationLocationCountry')),
                ('stationid', models.CharField(primary_key=True, max_length=64, serialize=False, db_column='StationID')),
                ('observationtimefriendly', models.CharField(max_length=256, blank=True, null=True, db_column='ObservationTimeFriendly')),
                ('observationdatetime', models.DateTimeField(blank=True, null=True, db_column='ObservationDateTime')),
                ('weatherdescription', models.CharField(max_length=64, blank=True, null=True, db_column='WeatherDescription')),
                ('temperature', models.DecimalField(blank=True, null=True, db_column='Temperature', max_digits=6, decimal_places=2)),
                ('relativehumidity', models.DecimalField(blank=True, null=True, db_column='RelativeHumidity', max_digits=3, decimal_places=2)),
                ('windstring', models.CharField(max_length=32, blank=True, null=True, db_column='WindString')),
                ('winddirection', models.CharField(max_length=16, blank=True, null=True, db_column='WindDirection')),
                ('winddegrees', models.SmallIntegerField(blank=True, null=True, db_column='WindDegrees')),
                ('windspeed', models.SmallIntegerField(blank=True, null=True, db_column='WindSpeed')),
                ('windgustspeed', models.SmallIntegerField(blank=True, null=True, db_column='WindGustSpeed')),
                ('pressuremb', models.IntegerField(blank=True, null=True, db_column='PressureMB')),
                ('pressurein', models.DecimalField(blank=True, null=True, db_column='PressureIN', max_digits=6, decimal_places=2)),
                ('dewpoint', models.SmallIntegerField(blank=True, null=True, db_column='Dewpoint')),
                ('windchill', models.SmallIntegerField(blank=True, null=True, db_column='WindChill')),
                ('feelslike', models.SmallIntegerField(blank=True, null=True, db_column='FeelsLike')),
                ('visibilitymiles', models.DecimalField(blank=True, null=True, db_column='VisibilityMiles', max_digits=10, decimal_places=2)),
                ('precipitationonehourin', models.DecimalField(blank=True, null=True, db_column='PrecipitationOneHourIN', max_digits=10, decimal_places=2)),
                ('precipitationdayin', models.DecimalField(blank=True, null=True, db_column='PrecipitationDayIN', max_digits=10, decimal_places=2)),
                ('iconname', models.CharField(max_length=32, blank=True, null=True, db_column='IconName')),
                ('iconurl', models.CharField(max_length=1024, blank=True, null=True, db_column='IconURL')),
                ('updatedatetime', models.DateTimeField(db_column='UpdateDateTime')),
            ],
            options={
                'db_table': 'Fact_WeatherCurrent',
                'managed': False,
            },
        ),
    ]
