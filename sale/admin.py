from django.contrib import admin
from .models import Customer, Sale, SalesPerson

# Register your models here.
admin.site.register(Customer)
admin.site.register(Sale)
admin.site.register(SalesPerson)
