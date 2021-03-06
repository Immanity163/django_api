from rest_framework import serializers
from .models import product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = product
        fields = ('id','title', 'description','price')