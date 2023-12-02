from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:id>/', views.cars, name='cars'),
    path('car/<int:id>/', views.car, name='car'),
]
