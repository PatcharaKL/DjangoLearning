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