from django.contrib import admin
from ecommerceapp.models import Contact, Product, Orders, OrderUpdate

# Register your models here.

# Registering Contact model
admin.site.register(Contact)

# Registering Product model
admin.site.register(Product)

# Registering Orders model
admin.site.register(Orders)

# Registering OrderUpdate model
admin.site.register(OrderUpdate)
