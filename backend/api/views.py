from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import  Product
from products.serializers import ProductSerializer
from django.http import JsonResponse
# Create your views here.

@api_view(['POST'])
def api_home(request):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance=serializer.save()
        # print(instance)
        return Response(serializer.data)
    return Response({'invalid':'not good data'},status=400)

# @api_view(['GET'])
# def api_home(request):
#     instance=Product.objects.all().order_by('?').first()
#     data={}
#     if instance:
#         data=ProductSerializer(instance).data
#     return Response(data)
