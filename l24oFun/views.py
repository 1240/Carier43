# -*- coding: utf-8 -*-
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from l24oFun.models import Product, ContactForm


def index(request):
    global for_thanks
    products = Product.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            body = " Номер телефона: {0} \n Продукт: {1} \n Кол-во: {2}".format(form.cleaned_data['phone_number'], form.cleaned_data['product'], form.cleaned_data['count'])
            email = EmailMessage("Заявка на сайте 'гравийпесок.рф'", body, "carierkirov43@gmail.com",
                                 to=["467686@mail.ru"])
            email.send()
            for_thanks = True
    else:
        for_thanks = False
        form = ContactForm()
    return render(request, 'main.html', {'products': products, 'form': form, "for_thanks": for_thanks})


def gravii(request):
    return render(request, 'gravii.html')