"""HereticFamily URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    
User Auth URLs
accounts/ login/ [name='login']
accounts/ logout/ [name='logout']
accounts/ password_change/ [name='password_change']
accounts/ password_change/done/ [name='password_change_done']
accounts/ password_reset/ [name='password_reset']
accounts/ password_reset/done/ [name='password_reset_done']
accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/ reset/done/ [name='password_reset_complete']
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
import HereticFamily.AppCode.Views.View_Home
import HereticFamily.AppCode.Views.View_Weather
import HereticFamily.AppCode.Views.View_Tasks

urlpatterns = [
    url(r'^$', HereticFamily.AppCode.Views.View_Home.home),
    url(r'^weather', HereticFamily.AppCode.Views.View_Weather.weather),
    url(r'^tasks', HereticFamily.AppCode.Views.View_Tasks.tasks),
    url(r'^taskUpdate', HereticFamily.AppCode.Views.View_Tasks.taskUpdate),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
]

