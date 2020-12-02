from django.shortcuts import render

from rest_framework import viewsets
from .serializers import UserSerializer, TravelSerializer
from .models import User, Travel

class TravelView(viewsets.ModelViewSet):
  serializer_class = TravelSerializer
  queryset = Travel.objects.all()
