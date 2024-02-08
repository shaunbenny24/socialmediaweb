from django.urls import path
from .views import PageListCreateAPIView, PageRetrieveUpdateDestroyAPIView

app_name = 'community'

urlpatterns = [
   path('pages/', PageListCreateAPIView.as_view(), name='page-list-create'),
    path('pages/<int:pk>/', PageRetrieveUpdateDestroyAPIView.as_view(), name='page-retrieve-update-destroy'),
]
