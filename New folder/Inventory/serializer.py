from rest_framework import serializers

from .models import *

class Products_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'