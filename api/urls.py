from django.contrib import admin
from django.urls import path, include
from .views.store import TiendaAPI
from .views.brands import MarcaAPI
from .views.deals import DealAPI
app_name = "api"
urlpatterns = [
    path("stores", TiendaAPI.as_view()),
    path("brands", MarcaAPI.as_view()),
    path("deals", DealAPI.as_view())
]
