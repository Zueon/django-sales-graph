from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone
from sale.utils import generate_code


# Customer Class to keep track of name and image
class Customer(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='customer')

    def __str__(self):
        return self.name

# SalesPerson class to keep track of the sales's person's infomation
class SalesPerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="No bio yet")
    avatar = models.ImageField(upload_to='avatars')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Salesperson {self.user.username}"


class Sale(models.Model):
    transaction_id = models.CharField(max_length=12, blank=True)
    total_price = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesman = models.ForeignKey(SalesPerson, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.transaction_id == "":
            self.transaction_id = generate_code()
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Sales for the amount of Kshs {self.total_price}"
