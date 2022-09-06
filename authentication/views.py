from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from . models import User
from . import serializers
# Create your views here.

class ThisIsHelloAuthView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={'message':"Hello Auth"})
        

class UserCreateView(generics.GenericAPIView):
    serializer_class = serializers.UserCreationSerializer

    def get(self, request):
        return Response(data={'message':"This is only for POST."})
    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status= status.HTTP_201_CREATED)
        return Response(data= serializer.errors, status = status.HTTP_400_BAD_REQUEST)