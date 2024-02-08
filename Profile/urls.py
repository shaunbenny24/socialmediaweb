from django.urls import path
# profile/urls.py
from django.urls import path
from .views import UserProfileAPIView


app_name = 'profile'


urlpatterns = [
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
]
