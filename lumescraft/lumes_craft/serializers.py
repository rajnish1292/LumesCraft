from rest_framework import serializers
from .models import *


class UserProfile_Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'


class Product_images_Serializer(serializers.ModelSerializer):
    product_image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = product_image
        fields = ('product_id', 'product_image')


class products_Serializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = (
            'category_id', 'product_id', 'product_name', 'SKU', 'product_price', 'description', 'warrenty_terms',
            'return_cancellation', 'dimensions', 'create_at', 'update_at')


class Wicker_Serializer(serializers.ModelSerializer):
    color_image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = wicker_color
        fields = ('wicker_id', 'color_name', 'color_image')


class Fabric_Serializer(serializers.ModelSerializer):
    color_image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = fabric_color
        fields = ('fabric_id', 'color_name', 'color_image')


class Frame_Serializer(serializers.ModelSerializer):
    color_image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = frame_color
        fields = ('frame_id', 'color_name', 'color_image')
