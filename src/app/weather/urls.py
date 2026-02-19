from django.urls import path
from .views import weather_list, weather_detail, current_weather, forecast_weather, seasonal_weather

urlpatterns = [
    path('', weather_list, name='weather-list'),
    path('<int:pk>/', weather_detail, name='weather-detail'),
    path('current/', current_weather, name='weather-current'),
    path('forecast/', forecast_weather, name='weather-forecast'),
    path('seasonal/', seasonal_weather, name='weather-seasonal'),
]
