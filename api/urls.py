from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('show-products/', views.showAllProducts, name='showProducts'),
    path('product-detail/<int:pk>/', views.viewProduct, name='productDetail'),
    path('create-product/', views.createProduct, name='createProduct'),
    path('update-product/<int:pk>/', views.updateProduct, name='updateProduct'),
    path('delete-product/<int:pk>/', views.deleteProduct, name='deleteProduct'),
]