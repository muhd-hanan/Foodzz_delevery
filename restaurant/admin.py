from django.contrib import admin

from restaurant.models import StoreCategory, Store, Slider, FoodCategory, FoodItem



admin.site.register(StoreCategory)
admin.site.register(Store)
admin.site.register(FoodCategory)
admin.site.register(FoodItem)
admin.site.register(Slider)


