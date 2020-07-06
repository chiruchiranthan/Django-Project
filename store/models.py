from django.db import models


# Create your models here.

class gift_type(models.Model):
    Gift_type=models.CharField(max_length=10)
    Gift_description=models.CharField(max_length=150)
    def __str__(self):
     return self.Gift_type
class gift(models.Model):
    Gift_name = models.CharField(max_length=30)
    Gift_type = models.CharField(max_length=30)
    Gift_costprice = models.CharField(max_length=60)
    headshot = models.ImageField(upload_to='img/')
    def __str__(self):
     return self.Gift_name
   
class customer(models.Model):
    Customer_name=models.CharField(max_length=30)
    email = models.EmailField()
    Phone= models.CharField(max_length=10,default=None)
    Address= models.CharField(max_length=30)
    Password=models.CharField(max_length=10, blank=True)
    def __str__(self):
     return self.Customer_name
class employee(models.Model):
    e_name=models.CharField(max_length=30)
    e_sal = models.CharField(max_length=50)
    e_designation = models.CharField(max_length=60)
    def __str__(self):
     return self.e_name
class Order(models.Model):
    Customer_name=models.CharField(max_length=30)
    Gift_name = models.ForeignKey(gift, default=1, verbose_name="Giftname", on_delete=models.SET_DEFAULT)
    Quantity=models.CharField(max_length=30,default=1)
    def __str__(self):
     return self.Customer_name

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)