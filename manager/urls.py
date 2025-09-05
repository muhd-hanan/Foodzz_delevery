from django.urls import path
from manager import views

app_name = "manager"



urlpatterns = [
    path('', views.index, name="index"),
   
    path("store_category/", views.store_category, name="store_category"),
    path("delete_store_category/<int:id>/", views.delete_store_category, name="delete_store_category"),

    path("sliders/", views.sliders, name="sliders"),
    path("sliders/delete/<int:id>/", views.delete_slider, name="delete_slider"),

   path("offers/", views.offers, name="offers"),
   path("offers/delete/<int:pk>/", views.delete_offer, name="delete_offer"),

   path("stores/", views.add_store, name="store_list"),
   path("stores/delete/<int:id>/", views.delete_store, name="delete_store"),

     path("delivery-boys/", views.delivery_boys, name="dboylist"),

    path("delivery-boys/delete/<int:id>/", views.delete_delivery_boy, name="delete_delivery_boy"),

   path("customers/", views.customers, name="customers"),  
path("customers/delete/<int:id>/", views.delete_customer, name="delete_customer"),




]



  