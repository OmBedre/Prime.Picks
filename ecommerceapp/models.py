from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.CharField(max_length=500)
    phonenumber = PhoneNumberField()

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100,default='')
    subcategory = models.CharField(max_length=50,default='')
    price = models.PositiveIntegerField()
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/images')

    def __str__(self):
        return self.product_name