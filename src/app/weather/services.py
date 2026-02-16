import requests
from django.conf import settings
from django.core.cache import cache
from decimal import Decimal
from .models import WeatherCache


class WeatherService:
    BASE_URL = settings.WEATHER_API_BASE_URL
    CACHE_TIMEOUT = settings.WEATHER_CACHE_TIMEOUT

    @classmethod
    def get_weather_code_description(cls, code):
        weather_codes = {
            0: 'Clear sky',
            1: 'Mainly clear',
            2: 'Partly cloudy',
            3: 'Overcast',
            45: 'Foggy',
            48: 'Depositing rime fog',
            51: 'Light drizzle',
            53: 'Moderate drizzle',
            55: 'Dense drizzle',
            61: 'Slight rain',
            63: 'Moderate rain',
            65: 'Heavy rain',
            71: 'Slight snow',
            73: 'Moderate snow',
            75: 'Heavy snow',
            77: 'Snow grains',
            80: 'Slight rain showers',
            81: 'Moderate rain showers',
            82: 'Violent rain showers',
            85: 'Slight snow showers',
            86: 'Heavy snow showers',
            95: 'Thunderstorm',
            96: 'Thunderstorm with slight hail',
            99: 'Thunderstorm with heavy hail',
        }
        return weather_codes.get(code, 'Unknown')

    @classmethod
    def fetch_current_weather(cls, latitude, longitude):
        cache_key = f'weather_current_{latitude}_{longitude}'
        cached_data = cache.get(cache_key)
        
        if cached_data:
            return cached_data

        params = {
            'latitude': float(latitude),
            'longitude': float(longitude),
            'current': 'temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,rain,weather_code,cloud_cover,wind_speed_10m',
            'timezone': 'Africa/Dar_es_Salaam'
        }

        try:
            response = requests.get(cls.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            current = data.get('current', {})
            weather_data = {
                'temperature': current.get('temperature_2m'),
                'apparent_temperature': current.get('apparent_temperature'),
                'humidity': current.get('relative_humidity_2m'),
                'precipitation': current.get('precipitation'),
                'rain': current.get('rain'),
                'weather_code': current.get('weather_code'),
                'weather_description': cls.get_weather_code_description(current.get('weather_code', 0)),
                'cloud_cover': current.get('cloud_cover'),
                'wind_speed': current.get('wind_speed_10m'),
                'timestamp': current.get('time'),
            }
            
            cache.set(cache_key, weather_data, cls.CACHE_TIMEOUT)
            return weather_data

        except requests.RequestException as e:
            return {'error': f'Weather API error: {str(e)}'}

    @classmethod
    def fetch_forecast(cls, latitude, longitude, days=7):
        cache_key = f'weather_forecast_{latitude}_{longitude}_{days}'
        cached_data = cache.get(cache_key)
        
        if cached_data:
            return cached_data

        params = {
            'latitude': float(latitude),
            'longitude': float(longitude),
            'daily': 'temperature_2m_max,temperature_2m_min,precipitation_sum,rain_sum,weather_code',
            'timezone': 'Africa/Dar_es_Salaam',
            'forecast_days': days
        }

        try:
            response = requests.get(cls.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            daily = data.get('daily', {})
            forecast_data = {
                'dates': daily.get('time', []),
                'temperature_max': daily.get('temperature_2m_max', []),
                'temperature_min': daily.get('temperature_2m_min', []),
                'precipitation': daily.get('precipitation_sum', []),
                'rain': daily.get('rain_sum', []),
                'weather_codes': daily.get('weather_code', []),
            }
            
            cache.set(cache_key, forecast_data, cls.CACHE_TIMEOUT)
            return forecast_data

        except requests.RequestException as e:
            return {'error': f'Weather API error: {str(e)}'}

    @classmethod
    def update_attraction_weather_cache(cls, attraction):
        weather_data = cls.fetch_current_weather(attraction.latitude, attraction.longitude)
        
        if 'error' not in weather_data:
            cache_obj, created = WeatherCache.objects.get_or_create(attraction=attraction)
            cache_obj.temperature = weather_data.get('temperature')
            cache_obj.apparent_temperature = weather_data.get('apparent_temperature')
            cache_obj.precipitation = weather_data.get('precipitation')
            cache_obj.rain = weather_data.get('rain')
            cache_obj.weather_code = weather_data.get('weather_code')
            cache_obj.cloud_cover = weather_data.get('cloud_cover')
            cache_obj.wind_speed = weather_data.get('wind_speed')
            cache_obj.humidity = weather_data.get('humidity')
            cache_obj.save()
            
            return cache_obj
        
        return None
