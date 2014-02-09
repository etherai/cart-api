from django.contrib.auth.models import User
from rest_framework import serializers

from models import Address, Cart, Product, Order

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password', 'addresses','carts')
        write_only_fields = ('password',)

    def restore_object(self, attrs, instance=None):
        user = super(AccountSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ( 'first_name','last_name','street_address1','street_address2', 'city', 'state', 'phone', 'url')


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ( 'url', 'items',)

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ( 'url', 'product_name','status', 'our_price', 'original_price','image_url','origianl_url', 'html','options' )

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ( 'url', 'items','cart')

class AuditSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password', 'addresses','carts')
        write_only_fields = ('password',)
	depth = 3
