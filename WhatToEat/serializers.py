from rest_framework import serializers
from .models import CookingDish

class CookingDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookingDish
        fields = ('name', 'additional_details', 'date_added')
