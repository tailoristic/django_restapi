from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    category = serializers.CharField(max_length=100)
    
    def create(self,validate_data):
        return Product.objects.create(**validate_data)