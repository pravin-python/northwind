import os
import uuid
from django.db import models
from apps.orders.models import Supplier
from django.utils.deconstruct import deconstructible

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='category/images/', blank=True, null=True)

    class Meta:
        db_table = 'categories' 

    def __str__(self):
        return self.category_name or f"Category {self.category_id}"

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    
    supplier = models.ForeignKey(
        'orders.Supplier', on_delete=models.SET_NULL, blank=True, null=True, db_column='supplier_id'
    )
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, blank=True, null=True, db_column='category_id'
    )

    quantity_per_unit = models.CharField(max_length=100, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    units_in_stock = models.IntegerField(default=0)
    units_on_order = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=0)
    discontinued = models.BooleanField(default=False)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.product_name

@deconstructible
class ProductImagePath:
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = f"{uuid.uuid4().hex}.{ext}"
        return os.path.join("product", "images", str(instance.product.product_id), filename)



class ProductImage(models.Model):
    IMAGE_TYPES = [
        ('small', 'Small'),
        ('base', 'Base'),
        ('thumbnail', 'Thumbnail'),
        ('other', 'Other'),
    ]

    image_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='images', db_column='product_id'
    )
    image_type = models.CharField(max_length=10, choices=IMAGE_TYPES)
    image = models.ImageField(upload_to=ProductImagePath()) 
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'product_images'
        unique_together = [('product', 'image_type')]
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'image_type'],
                name='unique_image_type_per_product',
                condition=~models.Q(image_type='other')  # 'other' can be multiple
            )
        ]

    def __str__(self):
        return f"{self.product.product_name} - {self.image_type}"