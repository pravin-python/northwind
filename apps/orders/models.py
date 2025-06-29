from django.db import models
from apps.customers.models import Customer
from apps.employees.models import Employee

class Shipper(models.Model):
    shipper_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'shippers'

    def __str__(self):
        return self.company_name

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    contact_title = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    home_page = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'suppliers'

    def __str__(self):
        return self.company_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True, db_column='customer_id'
    )
    employee = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, blank=True, null=True, db_column='employee_id'
    )
    ship_via = models.ForeignKey(
        Shipper, on_delete=models.SET_NULL, blank=True, null=True, db_column='ship_via'
    )

    order_date = models.DateTimeField(blank=True, null=True)
    required_date = models.DateTimeField(blank=True, null=True)
    shipped_date = models.DateTimeField(blank=True, null=True)
    
    freight = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    ship_name = models.CharField(max_length=255, blank=True, null=True)
    ship_address = models.CharField(max_length=255, blank=True, null=True)
    ship_city = models.CharField(max_length=100, blank=True, null=True)
    ship_region = models.CharField(max_length=100, blank=True, null=True)
    ship_postal_code = models.CharField(max_length=20, blank=True, null=True)
    ship_country = models.CharField(max_length=100, blank=True, null=True)

    # ✅ ManyToManyField added here
    products = models.ManyToManyField(
        'products.Product',
        through='OrderDetail',
        related_name='orders'
    )

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return f"Order #{self.order_id}"

class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, db_column='order_id'
    )
    product = models.ForeignKey(
        'products.Product', on_delete=models.CASCADE, db_column='product_id'
    )
    quantity = models.IntegerField(default=1)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    class Meta:
        db_table = 'order_details'
        unique_together = (('order', 'product'),)

    def __str__(self):
        return f"Order #{self.order_id} - Product #{self.product_id}"