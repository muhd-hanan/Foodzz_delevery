# restaurant/views.py (or dboy/views.py if you separated apps)
from django.shortcuts import render, redirect, get_object_or_404
from .models import DeliveryBoy
from customer.models import Order
from django.db.models import Sum

def dashboard(request):
    dboy_id = request.session.get('dboy_id')
    if not dboy_id:
        return redirect('web:login')  

    dboy = DeliveryBoy.objects.get(id=dboy_id)

    # ✅ Show unassigned orders (ACCEPTED by restaurant, not yet taken by any dboy)
    available_orders = Order.objects.filter(status="ACCEPTED", delivery_boy__isnull=True)

    # ✅ Show this dboy’s assigned orders
    my_orders = Order.objects.filter(delivery_boy=dboy)

    # Hero stats
    new_orders_count = available_orders.count()
    total_orders_taken = my_orders.count()
    
    # Total earnings = 10% of sum of all completed orders of this dboy
    completed_earnings = my_orders.filter(status="COMPLETED").aggregate(total=Sum('total'))['total'] or 0
    total_earnings = round(completed_earnings * 0.1, 2)

    return render(request, "dboy/dboydashboard.html", {
        "dboy": dboy,
        "available_orders": available_orders,
        "my_orders": my_orders,
        "new_orders_count": new_orders_count,
        "total_orders_taken": total_orders_taken,
        "total_earnings": total_earnings,
    })


def accept_order(request, order_id):
    dboy_id = request.session.get('dboy_id')
    if not dboy_id:
        return redirect('web:login')

    dboy = DeliveryBoy.objects.get(id=dboy_id)
    order = get_object_or_404(Order, id=order_id)

    if order.delivery_boy is None:  # only if not already taken
        order.delivery_boy = dboy
        order.status = "Assign_Delevery_boy"
        order.save()

    return redirect("dboy:dashboard")


def mark_out_for_delivery(request, order_id):
    dboy_id = request.session.get('dboy_id')
    if not dboy_id:
        return redirect('web:login')

    dboy = DeliveryBoy.objects.get(id=dboy_id)
    order = get_object_or_404(Order, id=order_id, delivery_boy=dboy)

    if order.status == "Assign_Delevery_boy":
        order.status = "OUT_FOR_DELIVERY"
        order.save()

    return redirect("dboy:dashboard")


def mark_completed(request, order_id):
    dboy_id = request.session.get('dboy_id')
    if not dboy_id:
        return redirect('web:login')

    dboy = DeliveryBoy.objects.get(id=dboy_id)
    order = get_object_or_404(Order, id=order_id, delivery_boy=dboy)

    if order.status == "OUT_FOR_DELIVERY":
        order.status = "COMPLETED"
        order.save()

    return redirect("dboy:dashboard")