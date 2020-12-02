from rest_framework import serializers
from .models import User, Travel

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'login', 'name', 'lastName')

class TravelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Travel
    fields = ('id', 'user', 'description', 'name', 'date')
