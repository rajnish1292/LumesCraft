from django.shortcuts import render
from .models import *
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .serializers import category_Serializer, products_Serializer, Product_images_Serializer
from rest_framework.response import Response
# Create your views here.


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
        serializer_prod_image = serializer_prod_image.data # for furture
        # Products_insta = serializer.data + serializer_prod_image # for furture
        Products_insta = serializer.data
        return Response(Products_insta)