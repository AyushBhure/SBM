from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from .models import Item, WeatherData
from .serializers import ItemSerializer, WeatherDataSerializer
import requests
from django.conf import settings
import os

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class WeatherDataViewSet(viewsets.ModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

    @action(detail=False, methods=['post'])
    def fetch_weather(self, request):
        """Fetch weather data from OpenWeatherMap API and store it"""
        city = request.data.get('city', 'London')
        api_key = os.getenv('OPENWEATHER_API_KEY', 'your_api_key_here')
        
        if api_key == 'your_api_key_here':
            return Response({
                'error': 'OpenWeatherMap API key not configured'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather"
            params = {
                'q': city,
                'appid': api_key,
                'units': 'metric'
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Store weather data
            weather_data = WeatherData.objects.create(
                city=city,
                temperature=data['main']['temp'],
                humidity=data['main']['humidity'],
                description=data['weather'][0]['description']
            )
            
            serializer = WeatherDataSerializer(weather_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except requests.RequestException as e:
            return Response({
                'error': f'Failed to fetch weather data: {str(e)}'
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'error': f'An error occurred: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def dashboard(request):
    """Dashboard view with data visualization"""
    return render(request, 'items/dashboard.html')
