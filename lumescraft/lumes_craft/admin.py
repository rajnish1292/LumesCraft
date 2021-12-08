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
    list_display = ('category_id', 'category_name', 'category_image', 'create_at', 'update_at')


admin.site.register(category, categoryAdmin)


class productAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = (
    'category_id', 'product_id', 'product_name', 'SKU', 'product_price', 'description', 'warrenty_terms',
    'return_cancellation', 'length', 'width', 'height', 'create_at', 'update_at')


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


class quotationAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('quotation_id', 'user_id', 'details', 'invoice', 'create_at', 'update_at' )


admin.site.register(quotation, quotationAdmin)


class invoiceAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('invoice_id','quotation_id', 'invoice_doc', 'create_at', 'update_at' )


admin.site.register(create_invoice_file, invoiceAdmin)


class cushionAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('cushion_id', 'cushion_size', 'cushion_price')


admin.site.register(cushion, cushionAdmin)