from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password

class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=20)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    contact_title = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return self.company_name or self.customer_id

class CustomerPasswordHistory(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='passwords'
    )
    current_password = models.CharField(max_length=128)
    previous_password = models.CharField(max_length=128, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'customer_password_history'

    def __str__(self):
        return f"Password history for {self.customer.customer_id}"

    def save(self, *args, **kwargs):
        # Only hash if the password is not already hashed
        if not self.current_password.startswith("pbkdf2_sha256$"):
            self.current_password = make_password(self.current_password)
        if self.previous_password and not self.previous_password.startswith("pbkdf2_sha256$"):
            self.previous_password = make_password(self.previous_password)
        super().save(*args, **kwargs)
