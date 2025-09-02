from django.urls import path
from . import views

app_name = "dboy"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
   
    path("orders/<int:order_id>/accept/", views.accept_order, name="accept_order"),
   path("orders/<int:order_id>/out-for-delivery/", views.mark_out_for_delivery, name="out_for_delivery"),
path("orders/<int:order_id>/complete/", views.mark_completed, name="complete_order"),

]
