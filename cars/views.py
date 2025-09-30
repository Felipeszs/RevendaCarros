from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm


def cars_view(request):
    search = request.GET.get('search')
    
    if search:
        # busca por modelo ou por nome da marca
        cars = Car.objects.filter(model__icontains=search).order_by('model') | Car.objects.filter(brand__name__icontains=search).order_by('model')
    else:
        # mostra todos os carros se não tiver busca
        cars = Car.objects.all().order_by('model')
        
    return render(
        request,
        'Cars.html',
        {'cars': cars}
    )


def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('car')
    else:
        new_car_form = CarModelForm()
    return render(
        request,
        'new_car.html',
        {'new_car_form' : new_car_form}
    )