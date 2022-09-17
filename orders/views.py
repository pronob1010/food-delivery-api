from django.shortcuts import render
from rest_framework import generics, status 
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from orders.models import Order, User
from . import serializers
from rest_framework.permissions import IsAuthenticated

import orders
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
    permission_classes =[IsAuthenticated]
# get
    def get(self, request, order_id):
        order = get_object_or_404(Order, pk = order_id)
        serializer = self.serializer_class(instance = order)
        return Response(data = serializer.data, status = status.HTTP_200_OK)
#post
    def post(self, request, order_id):
        data = request.data
        serializer = self.serializer_class(data=data)
        user = request.user

        if serializer.is_valid():
            serializer.save(customer = user)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.data, status = status.HTTP_400_BAD_REQUEST)
#put
    def put(self, request, order_id):
        data = request.data 
        order = get_object_or_404(Order, pk = order_id)
        serializer = self.serializer_class(data=data, instance=order)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.data, status = status.HTTP_400_BAD_REQUEST)
    
#delete
    def delete(self, order_id):
        order = get_object_or_404(Order, pk=order_id)
        order.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


class UpdateOrderStatus(generics.GenericAPIView):
    serializer_class = serializers.OrderStatusUpdateSerializer

    def put(self, request, order_id):
        order = get_object_or_404(Order, pk = order_id)
        data = request.data
        serializer = self.serializer_class(data=data, instance=order)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status = status.HTTP_200_OK)
        
        return Response(data=serializer.data, status = status.HTTP_400_BAD_REQUEST)

class UserOrdersView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer

    def get(self, request, user_id):
        user = User.objects.get(pk= user_id)
        orders = Order.objects.all().filter(customer = user)
        serializer = self.serializer_class(instance=orders)
        return Response(data = serializer.data, status= status.HTTP_200_OK)
