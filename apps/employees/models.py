from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    title_of_courtesy = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    home_phone = models.CharField(max_length=30, blank=True, null=True)
    extension = models.CharField(max_length=10, blank=True, null=True)
    
    reports_to = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True, related_name='subordinates'
    )

    territories = models.ManyToManyField(
        'employees.Territory',  # 🔁 Correct string format
        through='EmployeeTerritory',
        related_name='employees'
    )

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return f"{self.first_name or ''} {self.last_name or ''}".strip()

class Region(models.Model):
    region_id = models.IntegerField(primary_key=True)
    region_description = models.CharField(max_length=255)

    class Meta:
        db_table = 'regions'

    def __str__(self):
        return self.region_description

class Territory(models.Model):
    territory_id = models.CharField(primary_key=True, max_length=50)
    territory_description = models.CharField(max_length=255)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, db_column='region_id'
    )

    class Meta:
        db_table = 'territories'

    def __str__(self):
        return self.territory_description

class EmployeeTerritory(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, db_column='employee_id'
    )
    territory = models.ForeignKey(
        Territory, on_delete=models.CASCADE, db_column='territory_id'
    )

    class Meta:
        db_table = 'employee_territories'
        unique_together = (('employee', 'territory'),)

    def __str__(self):
        return f"{self.employee_id} - {self.territory_id}"