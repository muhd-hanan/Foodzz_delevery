from django.urls import path
from restaurant import views

app_name = "restaurant"


urlpatterns = [
   path('dashboard/', views.dashboard, name="restdashboard"),
   path("store/<int:id>/edit/", views.edit_store, name="edit_store"),
     path("orders/<int:order_id>/accept/", views.store_accept_order, name="store_accept_order"),

   path("categories/", views.add_category, name="category_list"),
   path("categories/<int:pk>/delete/", views.delete_category, name="delete_category"),

   path("add_fooditem/", views.add_food_item, name="add_fooditem"),
   path("delete_fooditem/<int:pk>/", views.delete_fooditem, name="delete_fooditem"),



  
]