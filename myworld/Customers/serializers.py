from rest_framework import serializers
from .models import Customers, Products
class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields = ('customer_id','title','fname', 'lname','email','password','address','phone','gender','birth_date')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ('product_id','product_name','description', 'price','rating')