from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields=[
            'title',
            'content',
            'price' ,
        ]