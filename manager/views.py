from django.shortcuts import render, reverse, get_object_or_404 , redirect
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from restaurant.models import *

from .forms import StoreCategoryForm
from django.contrib import messages
from manager.forms import *
from customer.models import *



def index(request):
    instances = Order.objects.all()
    orders = instances.count()
    stores = Store.objects.count()
    customers = Customer.objects.count()
    delivery_boys = DeliveryBoy.objects.count()

    # ✅ calculate 6% commission only on completed orders
    earnings = 0
    for order in instances:
        if order.status == "COMPLETED":   # correct status
            earnings += (order.total * 0.06)   # 6% cut

    context = {
        "instances": instances,
        "orders": orders,
        "stores": stores,
        "customers": customers,
        "delivery_boys": delivery_boys,
        "earnings": round(earnings, 2),   # optional: 2 decimal points
    }
    return render(request, 'manager/index.html', context)


def order_list(request):
    orders = Order.objects.select_related("customer", "store", "address", "delivery_boy") \
                          .prefetch_related("orderitem_set")

    context = {
        "orders": orders
    }
    return render(request, "manager/index.html", context)
        

@login_required(login_url='/manager/login')
def store_category(request):
    if request.method == "POST":
        form = StoreCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("manager:store_category")  # reload page after saving
    else:
        form = StoreCategoryForm()

    instances = StoreCategory.objects.all()

    context = {
        "form": form,
        "instances": instances
    }
    return render(request, "manager/store_categories.html", context)

def delete_store_category(request, id):
    category = get_object_or_404(StoreCategory, id=id)
    category.delete()
    messages.success(request, "Store category deleted successfully.")
    return redirect("manager:store_category")

def sliders(request):
    if request.method == "POST":
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("manager:sliders")  # ✅ correct with namespace
    else:
        form = SliderForm()

    instances = Slider.objects.all()
    return render(request, "manager/sliders.html", {"form": form, "instances": instances})

def delete_slider(request, id):
    slider = get_object_or_404(Slider, id=id)
    slider.delete()
    return redirect("manager:sliders")


def offers(request):
    if request.method == "POST":
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Offer added successfully.")
            return redirect("manager:offers")
    else:
        form = OfferForm()

    instances = Offer.objects.all()
    return render(request, "manager/offers.html", {
        "form": form,
        "instances": instances,
    })


def delete_offer(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    offer.delete()
    messages.success(request, "Offer deleted successfully.")
    return redirect("manager:offers")



def add_store(request):
    if request.method == "POST":
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            store = form.save()
            return redirect("manager:store_list")  # ✅ go back to list after adding
    else:
        form = StoreForm()

    stores = Store.objects.all()
    return render(request, "manager/store_list.html", {"form": form, "stores": stores})


def delete_store(request, id):
    store = get_object_or_404(Store, id=id)
    store.delete()
    return redirect("manager:store_list")


def delivery_boys(request):
    if request.method == "POST":
        form = DeliveryBoyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manager:dboylist")
    else:
        form = DeliveryBoyForm()

    delivery_boys = DeliveryBoy.objects.all()

    context = {
        "form": form,
        "delivery_boys": delivery_boys,
    }
    return render(request, "manager/dboylist.html", context = context)


def delete_delivery_boy(request, id):
    delivery_boy = get_object_or_404(DeliveryBoy, id=id)
    delivery_boy.delete()
    return redirect("manager:dboylist")


def customers(request):
    customers = Customer.objects.select_related("user").all()
    return render(request, "manager/customers.html", {"customers": customers})


def delete_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    user = customer.user
    customer.delete()
    user.delete()
    messages.success(request, "Customer and user account deleted successfully!")
    return redirect("manager:customers")