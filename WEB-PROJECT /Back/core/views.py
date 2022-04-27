from core.models import *
from core.serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse



class ProductsList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer2(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductLAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    # filter_backends = (filters.Search)


class OrdersListAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer2



@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, comp_id):
    try:
        company = Product.objects.get(id=comp_id)
    except Product.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = ProductSerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        company.delete()
        return Response({'deleted': True})


@api_view(['GET', 'POST'])
def reviews_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer2(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)@api_view(['GET', 'POST'])


class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def getUserByName(request,name):
    try:
        user = User.objects.get(username=name)
    except User.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = UserSerializer2(user)
        return Response(serializer.data)

@api_view(['GET'])
def getOrdersById(request,id):
    try:
        orders = Order.objects.filter(customer_id=id)
    except Order.DoesNotExist as e:
        return JsonResponse({'error':str(e)})
    if request.method == 'GET':
        serializer = OrderSerializer2(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'DELETE'])
def getOrderUserByIdOrder(request,id,order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = OrderSerializer2(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        order.delete()
        return Response({'deleted': True})




# class OrdersListByUserIdAPIView(generics.ListCreateAPIView):
#     queryset = Order.objects.get(customer_id=id)
#     serializer_class = OrderSerializer2

