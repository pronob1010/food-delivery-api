from django.urls import path 
from . views import ThisIsHelloAuthView
urlpatterns = [
    path('', ThisIsHelloAuthView.as_view(), name="auth"),
]