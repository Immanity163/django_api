from django.shortcuts import render

from rest_framework import viewsets

from .serializers import ProductSerializer
from .models import product

class ProductViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all().order_by('title')
    serializer_class = ProductSerializer