
from django.urls import path
from stands import views
from .views import SoldierList


urlpatterns = [
    path('', views.index, name='index'),
    path('soldiers/', SoldierList.as_view(), name='soldiers'),

]
