from rest_framework import viewsets
from .serializers import CustomerSerializer, ProductSerializer
from .models import Customers, Products
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer