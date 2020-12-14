from django.contrib import admin
from django.urls import path, include
from .views.store import TiendaAPI
from .views.brands import MarcaAPI
from .views.deals import DealAPI
from .views.user import UserAPI
from .views.auth import AuthAPI
app_name = "api"
urlpatterns = [
    path("stores", TiendaAPI.as_view()),
    path("brands", MarcaAPI.as_view()),
    path("deals", DealAPI.as_view()),
    path("user", UserAPI.as_view()),
    path("auth", AuthAPI.as_view())
]
