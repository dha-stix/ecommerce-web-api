from rest_framework.documentation import include_docs_urls
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('schema', get_schema_view(
        title="Ecommerce Application API",
        description="An API that contains images, prices and products, for E-commerce projects",
        version="1.0.0"
    ), name='openapi-schema'),
    path('docs/', include_docs_urls(title="Ecommerce Application API"))
]
