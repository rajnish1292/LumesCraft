from django.urls import include, path
from rest_framework import routers
from .views import category_ViewSet, Product_List_items


router = routers.DefaultRouter()
router.register(r'category_add', category_ViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('all_products/', Product_List_items.as_view({'get': 'list'})),

    ]