from django.urls import path
from . import views
urlpatterns = [
    path('', views.OrderCreateListView.as_view(), name='order'), 
    path('<int:order_id>/', views.OrderDetailsView.as_view(), name="order_details"),

]
