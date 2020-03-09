from django.urls import path
from stands import views
from .views import SoldierList, Amgt1Create

urlpatterns = [
    path('', views.index, name='index'),
    path('amgt1/add/', views.Amgt1Create.as_view(), name='amgt1'),
    path('soldiers/', SoldierList.as_view(), name='soldiers'),
]
