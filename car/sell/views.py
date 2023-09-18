from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . forms import *
from . models import car


def detail(request, pk):
    car = get_object_or_404(car,pk=pk)
    related_items = car.objects.filter(category=car.category,brand=car.brand, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'detail.html',{
        'car':car,
        'related_items':related_items
    })

@ login_required
def new(request):
    if request.method == 'POST':
        form = NewCarForm(request.POST, request.FILES)

        if form .is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('detail.html', pk=car.id)
    form = NewCarForm()

    context = {
        'form':form,
        'title':'New Car',
    }

    return render(request, 'sell.html', context)