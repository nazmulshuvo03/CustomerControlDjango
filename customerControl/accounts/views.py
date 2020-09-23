from django.shortcuts import render
from django.http import HttpResponse

# creating views
from .models import *


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

    context = {'customer': customer,
               'orders': orders, 'order_count': order_count}

    return render(req, 'accounts/customer.html', context)
