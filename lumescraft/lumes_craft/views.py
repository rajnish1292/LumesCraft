from django.shortcuts import render
from .models import *
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .serializers import category_Serializer, products_Serializer, Product_images_Serializer, Wicker_Serializer, \
    Fabric_Serializer, Frame_Serializer, UserProfile_Serializer
from rest_framework.response import Response


# Create your views here.


class User_Profile_List_items(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfile_Serializer

    def list(self, request, *args, **kwargs):
        user_profile_instance = UserProfile.objects.all()
        serializer = UserProfile_Serializer(user_profile_instance, many=True)
        user_profile_insta = serializer.data
        return Response(user_profile_insta)


class category_ViewSet(viewsets.ModelViewSet):
    queryset = category.objects.all()
    serializer_class = category_Serializer

    def post(self, request, format=None):
        serializer = category_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Product_List_items(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = products_Serializer, Product_images_Serializer

    def list(self, request, *args, **kwargs):
        Products_instance = product.objects.all()
        Products_image_instance = product_image.objects.all()
        serializer = products_Serializer(Products_instance, many=True)
        serializer_prod_image = Product_images_Serializer(Products_image_instance, many=True)
        serializer_prod_image = serializer_prod_image.data  # for furture
        # Products_insta = serializer.data + serializer_prod_image # for furture
        Products_insta = serializer.data
        return Response(Products_insta)


class Product_image_List_items(viewsets.ModelViewSet):
    queryset = product_image.objects.all()
    serializer_class = Product_images_Serializer

    def list(self, request, *args, **kwargs):
        product_image_instance = product_image.objects.all()
        serializer = Product_images_Serializer(product_image_instance, many=True, context={"request": request})
        product_image_insta = serializer.data
        return Response(product_image_insta)


class Category_List_items(viewsets.ModelViewSet):
    queryset = category.objects.all()
    serializer_class = category_Serializer

    def list(self, request, *args, **kwargs):
        category_instance = category.objects.all()
        serializer = category_Serializer(category_instance, many=True)
        category_insta = serializer.data
        return Response(category_insta)


class Wicker_List_items(viewsets.ModelViewSet):
    queryset = wicker_color.objects.all()
    serializer_class = Wicker_Serializer

    def list(self, request, *args, **kwargs):
        wicker_instance = wicker_color.objects.all()
        serializer = Wicker_Serializer(wicker_instance, many=True, context={"request": request})
        wicker_insta = serializer.data
        return Response(wicker_insta)


class Fabric_List_items(viewsets.ModelViewSet):
    queryset = fabric_color.objects.all()
    serializer_class = Fabric_Serializer

    def list(self, request, *args, **kwargs):
        fabric_instance = fabric_color.objects.all()
        serializer = Fabric_Serializer(fabric_instance, many=True, context={"request": request})
        fabric_insta = serializer.data
        return Response(fabric_insta)


class Frame_List_items(viewsets.ModelViewSet):
    queryset = frame_color.objects.all()
    serializer_class = Frame_Serializer

    def list(self, request, *args, **kwargs):
        frame_instance = frame_color.objects.all()
        serializer = Frame_Serializer(frame_instance, many=True, context={"request": request})
        frame_insta = serializer.data
        return Response(frame_insta)
