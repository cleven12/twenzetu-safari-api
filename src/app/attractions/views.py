from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.core.cache import cache
from .models import Attraction
from .serializers import (
    AttractionListSerializer,
    AttractionDetailSerializer,
    AttractionCreateUpdateSerializer
)

BASE_QUERYSET = Attraction.objects.filter(is_active=True).select_related('region', 'created_by').prefetch_related('images', 'tips')


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def attraction_list_create(request):
    if request.method == 'GET':
        attractions = BASE_QUERYSET
        search = request.query_params.get('search')
        if search:
            attractions = attractions.filter(name__icontains=search) | \
                          attractions.filter(description__icontains=search) | \
                          attractions.filter(short_description__icontains=search) | \
                          attractions.filter(region__name__icontains=search)
        ordering = request.query_params.get('ordering')
        if ordering:
            attractions = attractions.order_by(ordering)
        serializer = AttractionListSerializer(attractions, many=True)
        return Response(serializer.data)
    serializer = AttractionCreateUpdateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def attraction_detail(request, slug):
    try:
        attraction = BASE_QUERYSET.get(slug=slug)
    except Attraction.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AttractionDetailSerializer(attraction)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = AttractionCreateUpdateSerializer(attraction, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        attraction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def featured_attractions(request):
    cache_key = 'featured_attractions'
    featured = cache.get(cache_key)

    if not featured:
        featured_qs = BASE_QUERYSET.filter(is_featured=True)[:6]
        serializer = AttractionListSerializer(featured_qs, many=True)
        cache.set(cache_key, serializer.data, 3600)
        return Response(serializer.data)

    return Response(featured)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def attractions_by_category(request):
    category = request.query_params.get('category')
    if not category:
        return Response({'error': 'Category parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    attractions = BASE_QUERYSET.filter(category=category)
    serializer = AttractionListSerializer(attractions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def attractions_by_region(request):
    region_slug = request.query_params.get('region')
    if not region_slug:
        return Response({'error': 'Region parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    attractions = BASE_QUERYSET.filter(region__slug=region_slug)
    serializer = AttractionListSerializer(attractions, many=True)
    return Response(serializer.data)
