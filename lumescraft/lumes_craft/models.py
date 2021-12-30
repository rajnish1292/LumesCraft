from django.db import models
import jsonfield

# Create your models here.


class category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=500, blank=True)
    category_image = models.ImageField(upload_to="media/category")
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.category_id)


class product(models.Model):
    category_id = models.ForeignKey(category, on_delete=models.CASCADE)
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=500, blank=True)
    SKU = models.CharField(max_length=500, blank=True)
    product_price = models.CharField(max_length=500, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    warrenty_terms = models.TextField(max_length=1000, blank=True)
    return_cancellation = models.CharField(max_length=500, blank=True)
    length = models.CharField(max_length=500, blank=True)
    width = models.CharField(max_length=500, blank=True)
    height = models.CharField(max_length=500, blank=True)
    isTable = models.BooleanField(blank=True)
    topMaterial = models.CharField(max_length=500, blank=True)
    topPrice = models.CharField(max_length=500, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product_id)


class product_image(models.Model):
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="media/products_images")

    def __str__(self):
        return str(self.product_id)


class wicker_color(models.Model):
    wicker_id = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=500, blank=True)
    color_image = models.ImageField(upload_to="media/wicker")

    def __str__(self):
        return str(self.wicker_id)


class fabric_color(models.Model):
    fabric_id = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=500, blank=True)
    color_image = models.ImageField(upload_to="media/fabric")

    def __str__(self):
        return str(self.fabric_id)


class frame_color(models.Model):
    frame_id = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=500, blank=True)
    color_image = models.ImageField(upload_to="media/frame")

    def __str__(self):
        return str(self.frame_id)


class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=500, blank=True)
    email = models.EmailField(max_length=500, blank=True)
    phone = models.CharField(max_length=500, blank=True)
    alternate_phone = models.CharField(max_length=500, blank=True)
    address = models.TextField(max_length=500, blank=True)
    gstin = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return str(self.user_name)


class quotation(models.Model):
    quotation_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    details = jsonfield.JSONField()
    invoice = models.FileField(upload_to="media/invoice", blank=True)
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.quotation_id)


class cushion(models.Model):
    cushion_id = models.AutoField(primary_key=True)
    cushion_size = models.CharField(max_length=500, blank=True)
    cushion_price = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return str(self.cushion_id)


class invoice_save(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    invoice_link = models.CharField(max_length=1000, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.invoice_id)