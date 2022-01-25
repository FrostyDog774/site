from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('shipping', views.shipping, name='shipping'),
    path('refund', views.refund, name='refund'),
    path('privacy', views.privacy, name='privacy'),
]
