"""nursery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mauli import views
urlpatterns = [
    path("",views.index,name="home"),
    path("contact/",views.contact,name="contact"),
    path("order/",views.order,name="order"),
    path("about/",views.about,name="about"),
    path("cucumber/",views.cucumber,name="cucumber"),
    path("bringle/",views.bringle,name="bringle"),
    path("brocoli/",views.brocoli,name="brocoli"),
    path("cabbage/",views.cabbage,name="cabbage"),
    path("chilli/",views.chilli,name="chilli"),
    path("flower/",views.flower,name="flower"),
    path("marigold/",views.marigold,name="marigold"),
    path("tomato/",views.tomato,name="tomato"),
    path("watermelon/",views.watermelon,name="watermelon"),
    path("sugarcane/",views.sugarcane,name="sugarcane"),
    path("bittergourd/",views.bittergourd,name="bittergourd"),
]

