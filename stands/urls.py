
from django.urls import path
from stands import views

urlpatterns = [
    path('', views.index, name='index')
]
