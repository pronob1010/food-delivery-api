from django.urls import path 
from . views import ThisIsHelloAuthView
from . import views
urlpatterns = [
    path('', ThisIsHelloAuthView.as_view(), name="auth"),
    path('signup/', views.UserCreateView.as_view(), name="sign_up"),
]