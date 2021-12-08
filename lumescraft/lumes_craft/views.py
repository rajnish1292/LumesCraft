from django.shortcuts import render
from .models import *
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .serializers import category_Serializer, products_Serializer, Product_images_Serializer, Wicker_Serializer, \
    Fabric_Serializer, Frame_Serializer, UserProfile_Serializer, quotation_Serializer, UserSerializer, \
    RegisterSerializer, create_invoice_file_Serializer, cushion_Serializer
from rest_framework.response import Response
from django.http import Http404
from knox.models import AuthToken
from rest_framework import generics, permissions
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
import os
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice
import json, time
import ast

# Create your views here.


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


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
        serializer = category_Serializer(category_instance, many=True, context={"request": request})
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


class Cushion_List_items(viewsets.ModelViewSet):
    queryset = cushion.objects.all()
    serializer_class = cushion_Serializer

    def list(self, request, *args, **kwargs):
        cushion_instance = cushion.objects.all()
        serializer = cushion_Serializer(cushion_instance, many=True)
        cushion_insta = serializer.data
        return Response(cushion_insta)


class quotationDetail(APIView):

    def get_object(self, user_id):
        # Returns an object instance that should
        # be used for detail views.
        try:
            return quotation.objects.filter(user_id=user_id)
        except quotation.DoesNotExist:
            raise Http404

    def get(self, request, user_id, format=None):
        Accelerometer_obj = self.get_object(user_id)
        serializer = quotation_Serializer(Accelerometer_obj, many=True, context={"request": request})
        quotation_Serializer_insta = serializer.data

        return Response(quotation_Serializer_insta)


class quotation_ViewSet(viewsets.ModelViewSet):
    queryset = quotation.objects.all()
    serializer_class = quotation_Serializer

    def post(self, request, format=None):
        serializer = quotation_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class user_profile_add_ViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfile_Serializer

    def post(self, request, format=None):
        serializer = UserProfile_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


############################################## new changes ###############################

class product_baised_on_category(APIView):
    serializer_class = products_Serializer, Product_images_Serializer

    def get_object(self, category_id):
        # Returns an object instance that should
        # be used for detail views.
        try:
            return product.objects.filter(category_id=category_id)
        except product.DoesNotExist:
            raise Http404

    def get(self, request, category_id, format=None):
        product_obj = self.get_object(category_id)

        Local_url = "http://127.0.0.1:8000/media/"
        Server_url = "http://164.52.214.242:8009/media/"
        serializer = products_Serializer(product_obj, many=True, context={"request": request})
        product_Serializer_insta = serializer.data

        product_list = []
        for i in product_Serializer_insta:
            category_id = i['category_id']
            product_id = i['product_id']
            product_name = i['product_name']
            SKU = i['SKU']
            product_price = i['product_price']
            description = i['description']
            warrenty_terms = i['warrenty_terms']
            return_cancellation = i['return_cancellation']
            length = i['length']
            width = i['width']
            height = i['height']
            create_at = i['create_at']
            update_at = i['update_at']

            product_images = product_image.objects.filter(product_id=product_id).values_list('product_image', flat=True)
            # print("product_image ::", product_images)
            prod_images = []
            for PI in product_images:
                prod_images.append(Server_url + PI)

            product_dict = {
                'category_id': category_id,
                'product_id': product_id,
                'product_name': product_name,
                'SKU': SKU,
                'product_price': product_price,
                'description': description,
                'warrenty_terms': warrenty_terms,
                'return_cancellation': return_cancellation,
                'length': length,
                'width': width,
                'height': height,
                'create_at': create_at,
                'update_at': update_at,
                'product_images': prod_images

            }
            # print(product_dict)
            product_list.append(product_dict)
        return Response(product_list)

class create_invoice_file_view(APIView):

    def get_object(self, quotation_id):
        # Returns an object instance that should
        # be used for detail views.
        try:
            return quotation.objects.filter(quotation_id=quotation_id)
        except quotation.DoesNotExist:
            raise Http404

    def get(self, request, quotation_id, format=None):
        invoice_obj = self.get_object(quotation_id)
        serializer = create_invoice_file_Serializer(invoice_obj, many=True)
        invoice_obj_insta = serializer.data
        Local_url = "http://127.0.0.1:8000/media/"
        Server_url = "http://164.52.214.242:8009/media/"
        for i in invoice_obj_insta:
            deatils = i
            json_obj = json.dumps(deatils)
            res = json.loads(json_obj)

            # invoice_id = res['invoice_id']
            quotation_id = res['quotation_id']
            create_at = res['create_at']
            update_at = res['update_at']
            invoice_json = quotation.objects.filter(quotation_id=quotation_id).values_list('details', flat=True)
            invoice_json_list = []
            for IJ in invoice_json:
                json_data = ast.literal_eval(IJ)
                details = json.dumps(json_data)
                res = json.loads(details)
                result = self.invoice_create(res)
                invoice_link = Local_url+result
                create_invoice_file.objects.create(invoice_doc=invoice_link)
                Invoice = {
                    'quotation_id': quotation_id,
                    'invoice_url': invoice_link,
                    'create_at': create_at,
                    'update_at': update_at,
                }
                print("Invoice ::", Invoice)
                return Response(Invoice)

    def invoice_create(self, deatils):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        invoice_number = deatils['basic_information']['invoice_number']
        issue_date = deatils['basic_information']['issue_date']
        address = deatils['basic_information']['address']

        products_info = deatils['products_details']
        os.environ["INVOICE_LANG"] = "en"
        client = Client('Client company')
        provider = Provider('Lumes Craft',
                            'Address :: ' + address,
                            'Date :: ' + issue_date, bank_account='0000-0000-0000', bank_code='0000')

        creator = Creator('Lumes Craft')
        invoice = Invoice(client, provider, creator)
        filename = "media/invoice/"+timestr + ".pdf"
        for prod_info in products_info:
            desc = prod_info['item_name']
            price_per_unit = prod_info['price_per_unit']
            quantity = prod_info['quantity']
            invoice.add_item(Item(quantity, price_per_unit, description=desc))
            invoice.currency = "Rs."
            invoice.number = invoice_number
            docu = SimpleInvoice(invoice)
            docu.gen(filename, generate_qr_code=True)
        return filename