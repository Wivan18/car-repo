from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . forms import *
from . models import car


def detail(request, pk):
    cars = get_object_or_404(car, pk=pk)
    #Other_cars = car.objects.filter(category = car.category, is_sold=False).exclude(pk=pk)[0:3]
    context = {
        'cars':cars,
        #'Other_cars':Other_cars
    }
    return render(request, 'detail.html',context)

@ login_required
def sell(request):
   if request.method == 'POST':
        form = NewCarForm(request.POST, request.FILES)

        if form.is_valid():
            car = form.save(commit=False)
            car.created_by = request.user
            car.save()

            return redirect( 'buy.html', pk=car.id)
   else:
        form = NewCarForm()
        

        context = {
            'form':form,
            'title':'New Car',
        }

        return render(request, 'sell.html', context)


def edit(request, pk):
    car = get_object_or_404(car, pk=pk, created_by=request.user)

    if request.method =='POST':
        form = EditCarForm(request.POST, request.FILES, instance=car)

        if form.is_valid():
            form.save()

            return redirect('car:detail', pk=car.id)
    else:
        form = EditCarForm(instance=car)
     

    return render(request, 'car/form.html',{
        'form':form,
        'title':'Edit car'
    })

@login_required
def delete(request, pk):
    car = get_object_or_404(car, pk=pk, created_by=request.user)
    car.delete()


    return redirect('dashboard:index')