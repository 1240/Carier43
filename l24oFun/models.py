# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from l24oFun.validators import PhoneField


class Product(models.Model):
    name = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return str.format("{0} {1} {2}", self.name, str(self.price), "руб.")

class ContactForm(forms.Form):
    name = forms.CharField(required=True, label="ФИО")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = PhoneField(required=True, label="Номер телефона", validators=[phone_regex])
    product = forms.ModelChoiceField(required=True, queryset=Product.objects.all(), label="Продукт")
    count = forms.IntegerField(min_value=1, required=True, label="Количество")


