from django.db import models

from users.models import User

from restaurant.models import Store, FoodItem





class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email



class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=355)
    address_type = models.CharField(max_length=255)
    landmark = models.CharField(max_length=200)
    latitude = models.FloatField(null=True, blank=True) 
    longitude = models.FloatField(null=True, blank=True)
    appartment = models.CharField(max_length=255)  
    phone_number = models.CharField(max_length=15)
    
    is_selected = models.BooleanField(default=False)  

    class Meta:
        db_table = 'customer_address'
        verbose_name = 'address'
        verbose_name_plural = 'addresses'
        ordering = ['-id']

    def __str__(self):
        return self.customer.user.email

    def save(self, *args, **kwargs):
        if self.phone_number:
            # Store only digits, remove extra symbols like :" etc.
            self.phone_number = ''.join(filter(str.isdigit, self.phone_number))
        super().save(*args, **kwargs)


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    qty = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    amnt = models.FloatField()


    class Meta:
        db_table = 'customer_cart'
        verbose_name = 'cart'
        verbose_name_plural = 'carts'
        ordering = ['-id']


    def __str__(self):
        return self.product.name
    

class CartBill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    offer_amnt = models.FloatField(default=0, null=True, blank=True)
    delivery_charge = models.FloatField(default=0)
    coupen_code = models.CharField(max_length=255, null=True, blank=True)


    class Meta:
        db_table = 'customer_cart_bill'
        verbose_name = 'cart bill'
        verbose_name_plural = 'cart bills'
        ordering = ['-id']


    def __str__(self):
        return self.customer.user.email
    


class Order(models.Model):
    STATUS_CHOICES = [
        ('PLACED', 'Placed'),
        ('ACCEPTED', 'Accepted'),
        ('OUT_FOR_DELIVERY', 'Out for Delivery'),
        ('COMPLETED', 'Delivered'),
       
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    sub_total = models.FloatField()
    total = models.FloatField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    delivery_charge = models.IntegerField(default=0)
    delivery_boy = models.ForeignKey('dboy.DeliveryBoy', null=True, blank=True, on_delete=models.SET_NULL)

    # ✅ Add this back
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PLACED')

    class Meta:
        db_table = 'customer_order'
        ordering = ['-id']  


class OrderItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    qty = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    amnt = models.FloatField()
    

    class Meta:
        db_table = 'customer_order_item'
        verbose_name = 'order item'
        verbose_name_plural = 'order items'
        ordering = ['-id']


    def __str__(self):
        return self.customer.user.email
    

class Offer(models.Model):
    coupon_code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    offer = models.IntegerField()
    is_percentage = models.BooleanField(default=False)


    class Meta:
        db_table = 'offer_table'
        verbose_name = 'offer'
        verbose_name_plural = 'offers'
        ordering = ['-id']


    def __str__(self):
        return self.coupon_code
    
    

  


