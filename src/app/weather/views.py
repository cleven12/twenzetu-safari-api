from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.attractions.models import Attraction
from .models import WeatherCache, SeasonalWeatherPattern
from .serializers import WeatherCacheSerializer, SeasonalWeatherPatternSerializer, CurrentWeatherSerializer
from .services import WeatherService


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def weather_list(request):
    weather_caches = WeatherCache.objects.all()
    serializer = WeatherCacheSerializer(weather_caches, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def weather_detail(request, pk):
    try:
        weather_cache = WeatherCache.objects.get(pk=pk)
    except WeatherCache.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = WeatherCacheSerializer(weather_cache)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def current_weather(request):
    lat = request.query_params.get('lat')
    lon = request.query_params.get('lon')
    attraction_slug = request.query_params.get('attraction')

    if attraction_slug:
        try:
            attraction = Attraction.objects.get(slug=attraction_slug)
            lat = attraction.latitude
            lon = attraction.longitude
        except Attraction.DoesNotExist:
            return Response({'error': 'Attraction not found'}, status=status.HTTP_404_NOT_FOUND)

    if not lat or not lon:
        return Response(
            {'error': 'Latitude and longitude or attraction slug required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    weather_data = WeatherService.fetch_current_weather(lat, lon)

    if 'error' in weather_data:
        return Response(weather_data, status=status.HTTP_503_SERVICE_UNAVAILABLE)

    serializer = CurrentWeatherSerializer(data=weather_data)
    serializer.is_valid()
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def forecast_weather(request):
    lat = request.query_params.get('lat')
    lon = request.query_params.get('lon')
    days = request.query_params.get('days', 7)
    attraction_slug = request.query_params.get('attraction')

    if attraction_slug:
        try:
            attraction = Attraction.objects.get(slug=attraction_slug)
            lat = attraction.latitude
            lon = attraction.longitude
        except Attraction.DoesNotExist:
            return Response({'error': 'Attraction not found'}, status=status.HTTP_404_NOT_FOUND)

    if not lat or not lon:
        return Response(
            {'error': 'Latitude and longitude or attraction slug required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    forecast_data = WeatherService.fetch_forecast(lat, lon, int(days))

    if 'error' in forecast_data:
        return Response(forecast_data, status=status.HTTP_503_SERVICE_UNAVAILABLE)

    return Response(forecast_data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def seasonal_weather(request):
    attraction_slug = request.query_params.get('attraction')

    if not attraction_slug:
        return Response(
            {'error': 'Attraction slug required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        attraction = Attraction.objects.get(slug=attraction_slug)
        patterns = SeasonalWeatherPattern.objects.filter(attraction=attraction)
        serializer = SeasonalWeatherPatternSerializer(patterns, many=True)
        return Response(serializer.data)
    except Attraction.DoesNotExist:
        return Response({'error': 'Attraction not found'}, status=status.HTTP_404_NOT_FOUND)
