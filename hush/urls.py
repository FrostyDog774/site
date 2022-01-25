from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='hush'),
    path('shipping', views.shipping, name='shipping'),
    path('refund', views.refund, name='refund'),
    path('privacy', views.privacy, name='privacy'),
]
