from rest_framework import serializers
from .models import Customers
class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields = ('customer_id','title','fname', 'lname','email','password','address','phone','gender','birth_date')