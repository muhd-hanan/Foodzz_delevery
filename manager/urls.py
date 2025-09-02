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



    



    # path('store_category/',views.store_category,name='store_category'),
    # path('store_category_create/',views.store_category_create,name='store_category_create'),
    # path('store_category_update/<int:id>/',views.store_category_update,name='store_category_update'),
    # path('store_category_delete/<int:id>/',views.store_category_delete,name='store_category_delete'),



    # path('store/',views.store,name='store'),
    # path('single_store/<int:id>/',views.single_store,name='single_store'),
    # path('store_create/',views.store_create,name='store_create'),
    # path('store_update/<int:id>/',views.store_update,name='store_update'),
    # path('store_delete/<int:id>/',views.store_delete,name='store_delete'),



    # path('order/<int:id>/',views.order,name='order'),
    # path('order_assign/<int:id>/',views.order_assign,name='order_assign'),
    # path('order_accept/<int:id>/',views.order_accept,name='order_accept'),
    # path('order_reject/<int:id>/',views.order_reject,name='order_reject'),
    # path('order_prepared/<int:id>/',views.order_prepared,name='order_prepared'),
    # path('order_picked/<int:id>/',views.order_picked,name='order_picked'),
    # path('order_completed/<int:id>/',views.order_completed,name='order_completed'),




    # path('food_category/',views.food_category,name='food_category'),
    # path('food_category_create/',views.food_category_create,name='food_category_create'),
    # path('food_category_update/<int:id>/',views.food_category_update,name='food_category_update'),
    # path('food_category_delete/<int:id>/',views.food_category_delete,name='food_category_delete'),




    # path('food_item/',views.food_item,name='food_item'),
    # path('food_item_create/',views.food_item_create,name='food_item_create'),
    # path('single_food_item/<int:id>',views.single_food_item,name='single_food_item'),
    # path('food_item_update/<int:id>/',views.food_item_update,name='food_item_update'),
    # path('food_item_delete/<int:id>/',views.food_item_delete,name='food_item_delete'),

    


    # path('slider/',views.slider,name='slider'),
    # path('slider_create/',views.slider_create,name='slider_create'),
    # path('slider_update/<int:id>/',views.slider_update,name='slider_update'),
    # path('slider_delete/<int:id>/',views.slider_delete,name='slider_delete'),
