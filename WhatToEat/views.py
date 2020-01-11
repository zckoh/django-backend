from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CookingDishSerializer
from .models import CookingDish

class CookingDishView(viewsets.ModelViewSet):
    serializer_class = CookingDishSerializer
    queryset = CookingDish.objects.all()
