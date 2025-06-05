from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FavoriteCity
from .serializers import FavoriteCitySerializer
from .utils import get_weather_data

class FavoriteCityViewSet(viewsets.ModelViewSet):
    queryset = FavoriteCity.objects.all()
    serializer_class = FavoriteCitySerializer

@api_view(['GET'])
def get_weather(request, city_name):
    weather_data = get_weather_data(city_name)
    if weather_data:
        return Response(weather_data)
    else:
        return Response({"error": "Failed to fetch weather data"}, status=500)
