from django.contrib import admin
from .models import WeatherCache, SeasonalWeatherPattern


@admin.register(WeatherCache)
class WeatherCacheAdmin(admin.ModelAdmin):
    list_display = ['attraction', 'temperature', 'precipitation', 'last_updated']
    readonly_fields = ['last_updated']
    search_fields = ['attraction__name']


@admin.register(SeasonalWeatherPattern)
class SeasonalWeatherPatternAdmin(admin.ModelAdmin):
    list_display = ['attraction', 'season_type', 'start_month', 'end_month', 'avg_temperature', 'avg_rainfall']
    list_filter = ['season_type']
    search_fields = ['attraction__name']
