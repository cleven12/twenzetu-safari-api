from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.core.cache import cache
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiResponse
from .models import Attraction
from .serializers import (
    AttractionListSerializer,
    AttractionDetailSerializer,
    AttractionCreateUpdateSerializer
)

BASE_QUERYSET = Attraction.objects.filter(is_active=True).select_related('region', 'created_by').prefetch_related('images', 'tips')


@extend_schema(
    tags=['Attractions'],
    summary='List or create attractions',
    description=(
        '**GET** — Returns all active attractions. Supports optional query parameters:\n\n'
        '| Parameter | Type | Description |\n'
        '|-----------|------|-------------|\n'
        '| `search` | string | Filter by name, description, short description, or region name |\n'
        '| `ordering` | string | Sort by any field. Prefix with `-` for descending (e.g. `-created_at`) |\n\n'
        '**POST** — Create a new attraction. Requires authentication.\n\n'
        '**curl GET example:**\n'
        '```bash\n'
        'curl "https://cf89615f228bb45cc805447510de80.pythonanywhere.com/api/v1/attractions/?search=kilimanjaro"\n'
        '```\n\n'
        '**curl POST example:**\n'
        '```bash\n'
        'curl -X POST https://cf89615f228bb45cc805447510de80.pythonanywhere.com/api/v1/attractions/ \\\n'
        '  -H "Authorization: Bearer <access_token>" \\\n'
        '  -H "Content-Type: application/json" \\\n'
        '  -d \'{"name":"Ngorongoro Crater","slug":"ngorongoro-crater","region":1,"category":"wildlife",'
        '"description":"...","short_description":"...","latitude":"-3.2","longitude":"35.5",'
        '"difficulty_level":"moderate","access_info":"By road from Arusha",'
        '"best_time_to_visit":"June-October","seasonal_availability":"Year-round",'
        '"estimated_duration":"1-2 days"}\'\n'
        '```'
    ),
    parameters=[
        OpenApiParameter('search', description='Filter by name, description, short description or region', required=False, type=str),
        OpenApiParameter('ordering', description='Sort results by field. Prefix with `-` for descending (e.g. `name`, `-created_at`)', required=False, type=str),
    ],
    request=AttractionCreateUpdateSerializer,
    responses={
        200: OpenApiResponse(response=AttractionListSerializer(many=True), description='List of active attractions.'),
        201: OpenApiResponse(response=AttractionCreateUpdateSerializer, description='Attraction created successfully.'),
        400: OpenApiResponse(description='Validation error — check required fields.'),
        401: OpenApiResponse(description='Authentication required for POST.'),
    },
    examples=[
        OpenApiExample(
            'Create attraction',
            request_only=True,
            value={
                'name': 'Ngorongoro Crater',
                'slug': 'ngorongoro-crater',
                'region': 1,
                'category': 'wildlife',
                'description': 'The world\'s largest inactive caldera, home to the Big Five.',
                'short_description': 'World\'s largest inactive volcanic caldera.',
                'latitude': '-3.2',
                'longitude': '35.5',
                'difficulty_level': 'moderate',
                'access_info': 'By road from Arusha (approx. 3 hours).',
                'best_time_to_visit': 'June-October',
                'seasonal_availability': 'Year-round',
                'estimated_duration': '1-2 days',
                'entrance_fee': '70.00',
                'requires_guide': True,
                'requires_permit': False,
            },
        )
    ],
)
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


@extend_schema(
    tags=['Attractions'],
    summary='Retrieve, update or delete an attraction',
    description=(
        'Look up an attraction by its `slug` (the URL-friendly name, e.g. `mount-kilimanjaro`).\n\n'
        '- **GET** — Public. Returns full attraction details including region, images, and tips.\n'
        '- **PUT** — Full update. All writable fields required. Authentication required.\n'
        '- **PATCH** — Partial update. Only send the fields you want to change. Authentication required.\n'
        '- **DELETE** — Remove the attraction. Authentication required.\n\n'
        '**curl GET example:**\n'
        '```bash\n'
        'curl https://cf89615f228bb45cc805447510de80.pythonanywhere.com/api/v1/attractions/mount-kilimanjaro/\n'
        '```\n\n'
        '**curl PATCH example:**\n'
        '```bash\n'
        'curl -X PATCH https://cf89615f228bb45cc805447510de80.pythonanywhere.com/api/v1/attractions/mount-kilimanjaro/ \\\n'
        '  -H "Authorization: Bearer <access_token>" \\\n'
        '  -H "Content-Type: application/json" \\\n'
        '  -d \'{"entrance_fee":"80.00"}\'\n'
        '```'
    ),
    responses={
        200: OpenApiResponse(response=AttractionDetailSerializer, description='Full attraction details.'),
        204: OpenApiResponse(description='Attraction deleted successfully.'),
        401: OpenApiResponse(description='Authentication required for write operations.'),
        404: OpenApiResponse(description='No attraction found with the given slug.'),
    },
    examples=[
        OpenApiExample(
            'Partial update — change entrance fee',
            request_only=True,
            value={'entrance_fee': '80.00'},
        )
    ],
)
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


@extend_schema(
    tags=['Attractions'],
    summary='Featured attractions',
    description=(
        'Returns up to 6 attractions marked as featured (`is_featured=true`).\n\n'
        'Results are cached in memory for **1 hour** — changes in the admin panel may take up to 1 hour to reflect here.\n\n'
        '**curl example:**\n'
        '```bash\n'
        'curl https://cf89615f228bb45cc805447510de80.pythonanywhere.com/api/v1/attractions/featured/\n'
        '```'
    ),
    responses={
        200: OpenApiResponse(response=AttractionListSerializer(many=True), description='Up to 6 featured attractions.'),
    },
)
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


@extend_schema(
    tags=['Attractions'],
    summary='Attractions by category',
    description=(
        'Returns all active attractions filtered by category.\n\n'
        '**Valid category values:** `mountain`, `beach`, `wildlife`, `cultural`, `historical`, '
        '`adventure`, `national_park`, `island`, `waterfall`, `lake`, `other`\n\n'
        '**curl example:**\n'
        '```bash\n'
        'curl "https://cf89615f228bb45cc805447510de80.pythonanywhere.com/api/v1/attractions/by_category/?category=national_park"\n'
        '```'
    ),
    parameters=[
        OpenApiParameter(
            'category',
            description='Category slug. One of: `mountain`, `beach`, `wildlife`, `cultural`, `historical`, `adventure`, `national_park`, `island`, `waterfall`, `lake`, `other`',
            required=True,
            type=str,
            enum=['mountain', 'beach', 'wildlife', 'cultural', 'historical', 'adventure', 'national_park', 'island', 'waterfall', 'lake', 'other'],
        ),
    ],
    responses={
        200: OpenApiResponse(response=AttractionListSerializer(many=True), description='Attractions in the given category.'),
        400: OpenApiResponse(description='`category` query parameter is required.'),
    },
)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def attractions_by_category(request):
    category = request.query_params.get('category')
    if not category:
        return Response({'error': 'Category parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    attractions = BASE_QUERYSET.filter(category=category)
    serializer = AttractionListSerializer(attractions, many=True)
    return Response(serializer.data)


@extend_schema(
    tags=['Attractions'],
    summary='Attractions by region',
    description=(
        'Returns all active attractions within a region, identified by its `slug`.\n\n'
        'Use `GET /api/v1/regions/` to list all available region slugs.\n\n'
        '**curl example:**\n'
        '```bash\n'
        'curl "https://cf89615f228bb45cc805447510de80.pythonanywhere.com/api/v1/attractions/by_region/?region=arusha"\n'
        '```'
    ),
    parameters=[
        OpenApiParameter(
            'region',
            description='Region slug (e.g. `arusha`, `zanzibar`, `kilimanjaro`). See `GET /api/v1/regions/` for all slugs.',
            required=True,
            type=str,
        ),
    ],
    responses={
        200: OpenApiResponse(response=AttractionListSerializer(many=True), description='Attractions in the given region.'),
        400: OpenApiResponse(description='`region` query parameter is required.'),
    },
)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def attractions_by_region(request):
    region_slug = request.query_params.get('region')
    if not region_slug:
        return Response({'error': 'Region parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    attractions = BASE_QUERYSET.filter(region__slug=region_slug)
    serializer = AttractionListSerializer(attractions, many=True)
    return Response(serializer.data)
