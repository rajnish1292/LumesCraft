from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin


# Register your models here.


class user_profileAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'email', 'phone', 'alternate_phone', 'address')


admin.site.register(UserProfile, user_profileAdmin)


def getFieldsModel(model):
    return [field.name for field in model._meta.get_fields()]


class categoryAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('category_id', 'category_name', 'create_at', 'update_at')


admin.site.register(category, categoryAdmin)


class productAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = (
    'category_id', 'product_id', 'product_name', 'SKU', 'product_price', 'description', 'warrenty_terms',
    'return_cancellation', 'dimensions', 'create_at', 'update_at')


admin.site.register(product, productAdmin)


class productimageAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('product_id', 'product_image')


admin.site.register(product_image, productimageAdmin)


class wicker_colorAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('wicker_id', 'color_name', 'color_image')


admin.site.register(wicker_color, wicker_colorAdmin)


class fabric_colorAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('fabric_id', 'color_name', 'color_image')


admin.site.register(fabric_color, fabric_colorAdmin)


class frame_colorAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('frame_id', 'color_name', 'color_image')


admin.site.register(frame_color, frame_colorAdmin)
