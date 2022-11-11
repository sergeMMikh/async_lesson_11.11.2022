from django.shortcuts import render
from django.http import HttpResponse

from .models import Product


def index(request):
    return HttpResponse('hi, this is me')


def products_list(request):
    products = Product.objects.all()
    return render(request, 'main/list.html', {'products': products})
