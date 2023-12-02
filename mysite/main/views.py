from django.shortcuts import render
from .models import Category, Car

# Create your views here.

def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', context={
        'categories': categories
    })


def cars(request, id):
    cars = Category.objects.filter(pk=id)
    return render(request, 'cars.html', context={
        'cars': cars
    })


def car(request, id):
    car = Car.objects.filter(pk=id)
    return render(request, 'car.html', context={
        'car': car
    })
