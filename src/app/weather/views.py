from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.attractions.models import Attraction
from .models import WeatherCache, SeasonalWeatherPattern
from .serializers import WeatherCacheSerializer, SeasonalWeatherPatternSerializer, CurrentWeatherSerializer
from .services import WeatherService


class WeatherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WeatherCache.objects.all()
    serializer_class = WeatherCacheSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def current(self, request):
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

    @action(detail=False, methods=['get'])
    def forecast(self, request):
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

    @action(detail=False, methods=['get'])
    def seasonal(self, request):
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
