from django.shortcuts import render

from menu.models import ThaiFoodWarm, ThaiFoodSalad, ThaiFoodDessert


def menu(request):
    dishes = ThaiFoodWarm.objects.all().order_by('price')
    salads = ThaiFoodSalad.objects.all().order_by('price')
    desserts = ThaiFoodDessert.objects.all().order_by('price')
    return render(request, 'menu/menu.html', {'dishes': dishes, 'salads': salads, 'desserts': desserts})


def home(request):
    return render(request, 'menu/home.html')