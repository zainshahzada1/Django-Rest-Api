from unicodedata import name
from rest_framework.reverse import reverse
from . import validators
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Product
class ProductSerializer(ModelSerializer):
    my_discount= serializers.SerializerMethodField(read_only=True)
    edit_url= serializers.SerializerMethodField(read_only=True)
    url=serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk')
    # email=serializers.EmailField(write_only=True)
    title = serializers.CharField(
        validators=[validators.validate_title_no_hello, validators.unique_product_title])    
    # name = serializers.CharField(source='title',read_only=True)
    class Meta:
        model=Product
        fields=[
            # 'user',
            'pk',
            # 'name',
            # 'email',
            'url',
            'edit_url',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
         
    # def validate_title(self,value):
    #     qs=Product.objects.filter(title__iexact=value)
    #     if qs:
    #         raise serializers.ValidationError(f'This {value} is already exist')
    #     return value
    # def create(self,validated_data):
    #     # email=validated_data.pop('email')
    #     obj=super().create(validated_data)
    #     # print(email,obj)
    #     return obj
    # def update(self, instance, validated_data):
    #     email=validated_data.pop('email')
    #     return super().update(instance,validated_data)

    def get_edit_url(self,obj):
        # return f'/api/products/{obj.pk}'
        request=self.context.get('request')
        if request is None:
            return None
        return reverse('product-update',kwargs={'pk':obj.pk},request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Product):
            return None
        return obj.get_discount()



# SerializerMethodField
# This is a read-only field. It gets its value by calling a method on the serializer class it is attached to. It can be used to add any sort of data to the serialized representation of your object.

# Signature: SerializerMethodField(method_name=None)

# method_name - The name of the method on the serializer to be called. If not included this defaults to get_ < field_name > .
# The serializer method referred to by the method_name argument should accept a single argument (in addition to self), which is the object being serialized. It should return whatever you want to be included in the serialized representation of the object. For example:

# from django.contrib.auth.models import User
# from django.utils.timezone import now
# from rest_framework import serializers

# class UserSerializer(serializers.ModelSerializer):
#     days_since_joined = serializers.SerializerMethodField()

#     class Meta:
#         model = User
#         fields = '__all__'

#     def get_days_since_joined(self, obj):
#         return (now() - obj.date_joined).days