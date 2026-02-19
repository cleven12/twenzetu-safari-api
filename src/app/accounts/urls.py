from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import register, login, user_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', user_profile, name='user_profile'),
]
