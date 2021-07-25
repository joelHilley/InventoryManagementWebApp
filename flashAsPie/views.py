from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.shortcuts import redirect
from .models import Order, Product, User



def home(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }

    return render(request, "home.html", context)



def order(request):
    orders = Order.objects.all()
    context = {
        "orders": orders
    }

    return render(request, "order.html", context)


# creating the employee view


def employee(request):
    employees = User.objects.all()
    context = {
        "employees" : employees
    }
    return render(request, 'staff.html', context)



