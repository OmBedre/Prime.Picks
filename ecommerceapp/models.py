from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.CharField(max_length=500)
    phonenumber = PhoneNumberField()

    def __str__(self):
        return self.name
