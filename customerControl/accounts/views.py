from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.forms import inlineformset_factory

# creating views
from .models import *
from .forms import OrderForm
from .filters import OrderFilter


def home(req):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers, 'total_customers': total_customers,
               'total_orders': total_orders, 'delivered': delivered, 'pending': pending}

    return render(req, 'accounts/dashboard.html', context)


def products(req):
    products = Product.objects.all()
    return render(req, 'accounts/products.html', {'products': products})


def customer(req, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(req.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer': customer,
               'orders': orders, 'order_count': order_count, 'myFilter': myFilter}

    return render(req, 'accounts/customer.html', context)


def createOrder(req, pk):
    OrderFormSet = inlineformset_factory(
        Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=pk)
    # form = OrderForm(initial={'customer': customer})
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if req.method == 'POST':
        # print('Printing POST: ', req.POST)
        # form = OrderForm(req.POST)
        formset = OrderFormSet(req.POST, instance=customer)

        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}

    return render(req, 'accounts/order_form.html', context)


def updateOrder(req, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if req.method == 'POST':
        # print('Printing POST: ', req.POST)
        form = OrderForm(req.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(req, 'accounts/order_form.html', context)


def deleteOrder(req, pk):
    order = Order.objects.get(id=pk)

    if req.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(req, 'accounts/delete.html', context)
