from rest_framework import generics,mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Product
from api.mixin import IsStaffEditorPermissionsMixin
from.serializers import ProductSerializer


class ProductListCreateApiView(IsStaffEditorPermissionsMixin
                            , generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def perform_create(self, serializer):
        # email = serializer.validated_data.pop('email')
        # print(email)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user,content=content)
    
    def get_queryset(self,*args,**kwargs):
        qs= super().get_queryset(*args, **kwargs)
        request=self.request
        if not request.user.is_authenticated:
            return Product.objects.none()
        return qs.filter(user=request.user)


class ProductDetailApiView(IsStaffEditorPermissionsMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductMixinView(IsStaffEditorPermissionsMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field='pk'
    def get(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class ProductUpdateApiView(IsStaffEditorPermissionsMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field='pk'
    
    def perform_update(self,serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title


class ProductDestroyApiView(IsStaffEditorPermissionsMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance) 
            

@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args,**kwargs):
    if request.method=='GET':
    # url_args??
    # get_request -> detail View
        if pk is not None:
            obj=get_object_or_404(Product,pk=pk)
            data=ProductSerializer(obj,many=False).data
            return Response(data)
    # list view
        queryset=Product.objects.all()
        data=ProductSerializer(queryset,many=True).data
        return Response(data)
    if request.method =='POST':
        # create an item 
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({'invalid':'not good data'},status=400)