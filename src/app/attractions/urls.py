from django.urls import path
from .views import (
    attraction_list_create,
    attraction_detail,
    featured_attractions,
    attractions_by_category,
    attractions_by_region,
)

urlpatterns = [
    path('', attraction_list_create, name='attraction-list-create'),
    path('featured/', featured_attractions, name='attraction-featured'),
    path('by_category/', attractions_by_category, name='attraction-by-category'),
    path('by_region/', attractions_by_region, name='attraction-by-region'),
    path('<slug:slug>/', attraction_detail, name='attraction-detail'),
]
