from django.db import models

# Create your models here.
class Customers(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
    birth_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'customers'
    
    def __str__(self):
        return self.fname


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField()
    rating = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'