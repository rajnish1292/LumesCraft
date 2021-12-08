from django.urls import include, path
from rest_framework import routers
from .views import category_ViewSet, Product_List_items, Category_List_items, Wicker_List_items, Fabric_List_items, \
    Frame_List_items, User_Profile_List_items, Product_image_List_items, quotationDetail, quotation_ViewSet, \
    user_profile_add_ViewSet, RegisterAPI, product_baised_on_category, Cushion_List_items, \
    Check_user_exist, invoice_save_file_link_view, get_invoice_link, UpdateUserProfile
from knox import views as knox_views
from .views import LoginAPI

router = routers.DefaultRouter()
router.register(r'category_add', category_ViewSet)
router.register(r'quotation_create', quotation_ViewSet)
router.register(r'add_user', user_profile_add_ViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('all_user/', User_Profile_List_items.as_view({'get': 'list'})),
    path('all_products/', Product_List_items.as_view({'get': 'list'})),
    path('all_products_images/', Product_image_List_items.as_view({'get': 'list'})),
    path('all_category/', Category_List_items.as_view({'get': 'list'})),
    path('all_wicker/', Wicker_List_items.as_view({'get': 'list'})),
    path('all_fabric/', Fabric_List_items.as_view({'get': 'list'})),
    path('all_frame/', Frame_List_items.as_view({'get': 'list'})),
    path('all_cushion/', Cushion_List_items.as_view({'get': 'list'})),
    path('quotation_detail/<str:user_id>/', quotationDetail.as_view()),
    path('product_get/<str:category_id>/', product_baised_on_category.as_view()),
    path('save_invoice_file_link/', invoice_save_file_link_view.as_view()),
    path('check_user_exist/<str:phone>/', Check_user_exist.as_view()),
    path('get_invoice_link/<str:user_id>/', get_invoice_link.as_view()),
    path('UpdateUserProfile/', UpdateUserProfile.as_view())

]
