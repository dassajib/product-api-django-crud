from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializers

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/products-list/',
        'Detail View': '/products-details/<int:id>/',
        'Create Product': '/create-product/',
        'Update Product': '/update-product/<int:id>/',
        'Delete Product': '/delete-product/<int:id>/',
    }

    return Response(api_urls);


@api_view(['GET'])
def showAllProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializers(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializers(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data);


@api_view(["POST"])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializers(instance=product, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data);


@api_view(['GET'])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response('Product deleted successfully')
