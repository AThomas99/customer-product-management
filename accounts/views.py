from django.shortcuts import render
from .models import *


def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    # These are statistical numbers for status.html
    total_orders = Order.objects.all().count()
    delivered = Order.objects.filter(status='Delivered').count()
    pending = Order.objects.filter(status='Pending').count()

    context = {
        'customers': customers,
        'orders': orders,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
        }
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'accounts/products.html', context)

def customers(request, pk):
    customers = Customer.objects.get(id=pk)

    customer_orders = customers.order_set.all()

    context = {
        'customers': customers,
        'customer_orders': customer_orders,
        }
    return render(request, 'accounts/customers.html', context)