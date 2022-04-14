from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator
# def validate_title(value):

#     qs = Product.objects.filter(title__iexact=value)
#     if qs:
#         raise serializers.ValidationError(f'This {value} is already exist')
#     return value

def validate_title_no_hello(value):
    if 'hello' in value.lower():
        raise serializers.ValidationError('Hello is not Allowed here')
    return value

unique_product_title=UniqueValidator(queryset=Product.objects.all(),lookup='iexact')