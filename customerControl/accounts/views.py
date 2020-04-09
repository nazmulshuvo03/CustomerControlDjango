from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return render(req, 'accounts/dashboard.html')

def products(req):
    return render(req, 'accounts/products.html')

def customer(req):
    return render(req, 'accounts/customer.html')
