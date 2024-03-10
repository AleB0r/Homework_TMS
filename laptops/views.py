from django.shortcuts import render, redirect
from django.urls import reverse

from laptops.models import Laptop


# Create your views here.

def laptops_list(request):
    laptops = Laptop.objects.all()
    return render(request, 'laptops.html', {'laptops': laptops})

def laptop_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        manufacturer = request.POST.get('manufacturer')
        price = request.POST.get('price')
        laptop = Laptop(name=name, manufacturer=manufacturer, price=price)
        laptop.save()
        return redirect('laptops_list')

    return render(request, 'laptop_add.html')