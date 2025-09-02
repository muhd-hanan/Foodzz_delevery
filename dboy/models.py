from django.db import models


from django.db import models
from django.contrib.auth.models import User  # or your CustomUser model
from restaurant.models import Store


class DeliveryBoy(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()


    class Meta:
        db_table = "delivery_boy"
        ordering = ['-id']

    def __str__(self):
        return self.name

# Create your models here.
