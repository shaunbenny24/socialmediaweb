from django.shortcuts import render

# Create your views here.
# community/views.py
from rest_framework import generics
from .models import Page
from .serializers import PageSerializer

class PageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
