
from rest_framework import serializers
from .models import Product, Category, Order, Review


class CategorySerializer(serializers.ModelSerializer):
   class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock', 'is_active', 'created_at', 'updated_at']



class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
   

    class Meta:
        model = Order
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = '__all__'

