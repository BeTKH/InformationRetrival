"""
URL configuration for textIrApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')


Including another URLconf ( !!!used this option!!!)
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

"""
map urls to the app components 

path ('nameOfApp/', include('path To the App url'))

"""

urlpatterns = [

    path('', views.getQueryText, name="getQueryText__"),
    path('', views.acceptUserQuery, name="acceptquery"),
    path('admin/', admin.site.urls),
    path('searchFunc/', include('searchFunc.urls')),
    path('tdm/', include('tdm.urls')),

]
