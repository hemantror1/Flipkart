from django.contrib import admin
from customer.models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(CustomerAddress)
admin.site.register(CustomerAdhar)


