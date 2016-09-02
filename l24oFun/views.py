# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from l24oFun.models import Product, ContactForm


def index(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
    return render(request, 'main.html', {'products': products, 'form': form})