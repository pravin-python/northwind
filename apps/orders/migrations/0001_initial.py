# Generated by Django 5.2 on 2025-06-29 09:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('shipper_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'shippers',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('contact_name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_title', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('fax', models.CharField(blank=True, max_length=30, null=True)),
                ('home_page', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'suppliers',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(blank=True, null=True)),
                ('required_date', models.DateTimeField(blank=True, null=True)),
                ('shipped_date', models.DateTimeField(blank=True, null=True)),
                ('freight', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('ship_name', models.CharField(blank=True, max_length=255, null=True)),
                ('ship_address', models.CharField(blank=True, max_length=255, null=True)),
                ('ship_city', models.CharField(blank=True, max_length=100, null=True)),
                ('ship_region', models.CharField(blank=True, max_length=100, null=True)),
                ('ship_postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('ship_country', models.CharField(blank=True, max_length=100, null=True)),
                ('customer', models.ForeignKey(blank=True, db_column='customer_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer')),
                ('employee', models.ForeignKey(blank=True, db_column='employee_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employee')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('order', models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
            options={
                'db_table': 'order_details',
            },
        ),
    ]
