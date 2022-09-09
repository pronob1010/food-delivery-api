from django.shortcuts import render
from rest_framework import generics, status 
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from orders.models import Order
from . import serializers
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class helloOrderView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message":"This is for orders!"}, status=status.HTTP_200_OK)

class OrderCreateListView(generics.GenericAPIView):
    serializer_class = serializers.OrderCreationSerializer
    queryset = Order.objects.all()
    permission_classes =[IsAuthenticated]

    def get(self, request):
        orders = Order.objects.all()
        serializer = self.serializer_class(instance=orders, many=True) 
        return Response(data = serializer.data, status= status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        user = request.user

        if serializer.is_valid():
            serializer.save(customer = user)
            return Response(data= serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors , status=status.HTTP_400_BAD_REQUEST)


class OrderDetailsView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    def get(self, request, order_id):
        order = get_object_or_404(Order, pk = order_id)
        serializer = self.serializer_class(instance = order)
        return Response(data = serializer.data, status = status.HTTP_200_OK)

    def post(self, request, order_id):
        data = request.data
        serializer = self.serializer_class(data=data)
        user = request.user

        if serializer.is_valid():
            serializer.save(customer = user)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.data, status = status.HTTP_400_BAD_REQUEST)

    # def put(self, request, order_id):
        # pass
