from django.urls import path
from .views import region_list_create, region_detail

urlpatterns = [
    path('', region_list_create, name='region-list-create'),
    path('<slug:slug>/', region_detail, name='region-detail'),
]
