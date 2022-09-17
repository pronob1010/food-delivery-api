from django.urls import path
from . import views
urlpatterns = [
    path('', views.OrderCreateListView.as_view(), name='order'), 
    path('<int:order_id>', views.OrderDetailsView.as_view(), name="order_details"),
    path('update-status/<int:order_id>/', views.UpdateOrderStatus.as_view(), name="update_order_status"),
    path('user/<int:user_id>/orders/', views.UserOrdersView.as_view(), name="user_order"),
]
