from django.urls import path
from . import views

urlpatterns = [
    path('Pune',views.Pune,name='pune'),
    path('Noida',views.Noida,name="noida")
]