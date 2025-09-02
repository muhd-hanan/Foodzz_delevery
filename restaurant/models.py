from django.db import models

from users.models import User   




class StoreCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='category')

    class Meta:
        db_table = 'restaurant_store_categoy'
        verbose_name = 'store category'
        verbose_name_plural = 'store categories'
        ordering = ['-id']

    def __str__(self):
        return self.name
    

class Store(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=256)
    tagline = models.CharField(max_length=256)
    categories = models.ManyToManyField(StoreCategory, related_name="stores")
    image = models.FileField(upload_to='store')
    rating = models.FloatField()
    time = models.IntegerField()
    offer = models.CharField(max_length=255)


    class Meta:
        db_table = 'restaurant_store'
        verbose_name = 'store'
        verbose_name_plural = 'stores'
        ordering = ['-id']


    def __str__(self):
        return self.name
    


class Slider(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='slide')
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


    class Meta:
        db_table = 'restaurant_slider'
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'
        ordering = ['-id']


    def __str__(self):
        return self.name
    


    


class FoodCategory(models.Model):
    name = models.CharField(max_length=255) 
    store = models.ForeignKey(Store, on_delete=models.CASCADE) 


    class Meta:
        db_table = 'food_category'
        verbose_name = 'food category'
        verbose_name_plural = 'food categories'
        ordering = ['id']


    def __str__(self):
        return self.name
    



class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    is_veg = models.BooleanField(default=False)
    price = models.IntegerField()
    image = models.FileField(upload_to='fooditems')
    categry = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='fooditem')


    class Meta:
        db_table = 'food_item'
        verbose_name = 'food item'
        verbose_name_plural = 'food items'
        ordering = ['id']


    def __str__(self):
        return self.name



