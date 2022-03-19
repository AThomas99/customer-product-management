from django.shortcuts import redirect, render
from django.forms import inlineformset_factory

from .models import *
from .forms import OrderForm
from .filters import OrderFilter

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
    myFilter = OrderFilter(request.GET, queryset=customer_orders)
    customer_orders = myFilter.qs

    context = {
        'customers': customers,
        'customer_orders': customer_orders,
        'myFilter': myFilter,
        }
    return render(request, 'accounts/customers.html', context)


def createOrder(request, pk):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
	customers = Customer.objects.get(id=pk)
	form = OrderFormSet(queryset=Order.objects.none(),instance=customers)
	#form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		#form = OrderForm(request.POST)
		form = OrderFormSet(request.POST, instance=customers)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'form':form, 'customers': customers}
	return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('home')

    context ={"form": form, 'order': order}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('home')
    return render(request, 'accounts/delete.html', {'item': order})