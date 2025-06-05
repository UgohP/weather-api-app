from django.urls import path
from .views import get_weather

urlpatterns = [
    path('weather/<str:city_name>/', get_weather, name='get_weather'),
]
