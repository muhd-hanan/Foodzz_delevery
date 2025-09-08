
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Store
from restaurant.form import *
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from customer.models import Store, Order, OrderItem
from django.db.models import Sum

def dashboard(request):
    store_id = request.session.get('store_id')
    if not store_id:
        return redirect('web:login')

    store = Store.objects.get(id=store_id)

    total_orders = Order.objects.filter(store=store).count()
    total_earnings = Order.objects.filter(store=store).aggregate(total=Sum('total'))['total'] or 0

    orders = (
        Order.objects.filter(store=store)
        .select_related('customer__user', 'address', 'delivery_boy')
        .prefetch_related('orderitem_set__product')
        .order_by('-id')
    )

    return render(request, 'store/restdashboard.html', {
        "store": store,
        "total_orders": total_orders,
        "total_earnings": total_earnings,
        "orders": orders,
    })


def store_accept_order(request, order_id):
    store_id = request.session.get('store_id')
    if not store_id:
        return redirect('web:login')

    store = get_object_or_404(Store, id=store_id)
    order = get_object_or_404(Order, id=order_id, store=store)

    if order.status != 'PLACED':
        messages.info(request, f"Order {order.order_id} is already {order.get_status_display()}.")
        return redirect('restaurant:restdashboard')

    order.status = 'ACCEPTED'
    order.save(update_fields=['status'])
    messages.success(request, f"Order {order.order_id} accepted.")
    return redirect("restaurant:restdashboard")


def edit_store(request, id):
    store = get_object_or_404(Store, id=id)

    if request.method == "POST":
        form = StoreEditForm(request.POST, request.FILES, instance=store)
        if form.is_valid():
            form.save()
            messages.success(request, "Store details updated successfully!")
            return redirect("store:restdashboard")  
    else:
        form = StoreEditForm(instance=store)

    return render(request, "store/edit_store.html", {"form": form, "store": store})


def add_category(request):
   
    store_id = request.session.get('store_id')
    if not store_id:
        return redirect("login")   

    store = Store.objects.get(id=store_id)

    if request.method == "POST":
        form = FoodCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.store = store  
            category.save()
            return redirect("restaurant:category_list")
    else:
        form = FoodCategoryForm()

   
    categories = (
        FoodCategory.objects.filter(store=store)
        .annotate(food_count=Count("fooditem"))
    )

    return render(request, "store/foodcategory.html", {
        "form": form,
        "categories": categories,
        "store": store
    })

def delete_category(request, pk):
    store_id = request.session.get("store_id")
    if not store_id:
        return redirect("login")

    store = Store.objects.get(id=store_id)
    category = get_object_or_404(FoodCategory, id=pk, store=store)

    if request.method == "POST":  
        category.delete()
        return redirect("restaurant:category_list")

    return render(request, "store/confirm_delete.html", {"category": category})



def add_food_item(request):
    store_id = request.session.get("store_id")
    if not store_id:
        return redirect("login")

    store = Store.objects.get(id=store_id)  

    if request.method == "POST":
        form = FoodItemForm(request.POST, request.FILES, store=store)  
        if form.is_valid():
            food_item = form.save(commit=False)
            food_item.save()
            return redirect("restaurant:add_fooditem")
    else:
        form = FoodItemForm(store=store)  

   
    fooditems = FoodItem.objects.filter(categry__store=store)

    return render(request, "store/add_fooditem.html", {
        "form": form,
        "store": store,
        "fooditems": fooditems,  
    })


def delete_fooditem(request, pk):
    store_id = request.session.get("store_id")
    if not store_id:
        return redirect("login")

    food_item = get_object_or_404(FoodItem, id=pk, categry__store_id=store_id)
    food_item.delete()
    return redirect("restaurant:add_fooditem")