# cart_app/serializers.py
from rest_framework import serializers
from .models import Cart, CartItem
from products_app.models import Product
from products_app.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    # Nested product info for read operations
    product = ProductSerializer(read_only=True)
    # Accept product ID for create/update
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product',
        write_only=True
    )

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'product_id', 'quantity']
        read_only_fields = ['id', 'cart', 'product']

    def create(self, validated_data):
        """
        Ensure the CartItem is linked to the cart in context.
        """
        cart = self.context.get('cart')
        if not cart:
            raise serializers.ValidationError("Cart context is required.")
        validated_data['cart'] = cart
        return super().create(validated_data)


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']
        read_only_fields = ['id', 'user', 'items']
