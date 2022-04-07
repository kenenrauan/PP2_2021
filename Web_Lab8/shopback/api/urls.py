from .views import category_detail, category_list, product_detail, product_list
from django.urls import path

urlpatterns = [
    path('products/', product_list),
    path('products/<int:id>/', product_detail),
    path('categories/', category_list),
    path('categories/<int:id>/', category_detail),
]