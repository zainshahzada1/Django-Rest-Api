from itertools import product
from unicodedata import name
from django.urls import path
from . import views
urlpatterns=[
    path('', views.ProductListCreateApiView.as_view(),name='product-list'),
    path('<int:pk>/update/', views.ProductUpdateApiView.as_view(),name='product-update'),
    path('<int:pk>/destroy/', views.ProductDestroyApiView.as_view()),
    path('<int:pk>/', views.ProductDetailApiView.as_view(),name='product-detail')
]