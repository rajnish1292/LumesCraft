from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

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
            'return_cancellation', 'length', 'width', 'height', 'create_at', 'update_at')


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


class quotation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = quotation
        fields = '__all__'


class invoice_save_file_Serializer(serializers.ModelSerializer):
    class Meta:
        model = invoice_save
        fields = '__all__'


class cushion_Serializer(serializers.ModelSerializer):
    class Meta:
        model = cushion
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user_id', 'user_name', 'email', 'alternate_phone', 'address', 'gstin']