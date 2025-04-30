from django.urls import path
from . import views# store/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('clothing/<int:pk>/', views.clothing_detail, name='clothing_detail'),
    path('category/<int:category_id>/', views.clothing_by_category, name='clothing_by_category'),
    path('cart/add/<int:clothing_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:clothing_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('order/', views.place_order, name='place_order'),
    path('myorders/', views.view_orders, name='view_orders'),
]
