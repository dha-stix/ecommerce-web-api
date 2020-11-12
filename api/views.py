from rest_framework.filters import SearchFilter
from .serializers import ProductSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Product

# Create your views here.

class ViewAllProducts(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ("name",  "category__category")



