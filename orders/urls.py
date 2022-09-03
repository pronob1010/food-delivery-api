from django.urls import path
from . views import helloOrderView
urlpatterns = [
    path('', helloOrderView.as_view(), name='order')
]
