from django.urls import include, path
from rest_framework import routers
from .views import category_ViewSet, Product_List_items, Category_List_items, Wicker_List_items, Fabric_List_items, \
    Frame_List_items, User_Profile_List_items, Product_image_List_items

router = routers.DefaultRouter()
router.register(r'category_add', category_ViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('all_user/', User_Profile_List_items.as_view({'get': 'list'})),
    path('all_products/', Product_List_items.as_view({'get': 'list'})),
    path('all_products_images/', Product_image_List_items.as_view({'get': 'list'})),
    path('all_category/', Category_List_items.as_view({'get': 'list'})),
    path('all_wicker/', Wicker_List_items.as_view({'get': 'list'})),
    path('all_fabric/', Fabric_List_items.as_view({'get': 'list'})),
    path('all_frame/', Frame_List_items.as_view({'get': 'list'})),

]
