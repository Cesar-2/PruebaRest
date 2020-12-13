from django.contrib import admin
from django.urls import path, include
from .views.store import TiendaAPI
from .views.brands import MarcaAPI
app_name = "api"
urlpatterns = [
    path("stores", TiendaAPI.as_view()),
    path("brands", MarcaAPI.as_view())
]
