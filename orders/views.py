from django.shortcuts import render
from rest_framework import generics, status 
from rest_framework.response import Response
# Create your views here.


class helloOrderView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message":"This is for orders!"}, status=status.HTTP_200_OK)

