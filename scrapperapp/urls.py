from django.contrib import admin
from django.urls import path
from scrapperapp.views import home
from scrapperapp.views import bootcamp

urlpatterns = [
    path('home/',home),
    path('bootcamp/',bootcamp)
]
