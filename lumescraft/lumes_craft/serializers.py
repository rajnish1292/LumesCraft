from rest_framework import serializers
from .models import *


class category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'


class Product_images_Serializer(serializers.ModelSerializer):
    class Meta:
        model = product_image
        fields = '__all__'

class products_Serializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = (
                'category_id', 'product_id', 'product_name', 'SKU', 'product_price', 'description', 'warrenty_terms',
                'return_cancellation', 'dimensions', 'create_at', 'update_at')