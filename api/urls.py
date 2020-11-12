from .views import ViewAllProducts
from django.urls import path

urlpatterns = [
    path('', ViewAllProducts.as_view(), name="products"),
]
