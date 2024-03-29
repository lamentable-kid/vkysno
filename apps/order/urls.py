from django.urls import path
from apps.order import views


urlpatterns = [
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('cart_view/', views.show_cart, name='show_cart'),
    path('create/', views.create_order, name='create_order'),
    path('delete/<int:row_id>/', views.delete_from_cart, name='delete_from_cart'),
]
