from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('inoske', views.inoske, name='inoske'),
    path('zenitsu', views.zenitsu, name='zenitsu'),
    path('rengoku', views.rengoku, name='rengoku'),
    path('muichiro', views.muichiro, name='muichiro'),
    path('shinobu', views.shinobu, name='shinobu'),
    path('expl', views.expl, name='expl'),
    path('shipping', views.shipping, name='shipping'),
    path('refund', views.refund, name='refund'),
    path('privacy', views.privacy, name='privacy'),
]
