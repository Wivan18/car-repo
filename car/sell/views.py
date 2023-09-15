from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . forms import *
from . models import car

# Create your views here.
@ login_required
def new(request):
    form = NewCarForm

    context = {
        'form':form,
        'title':'New Car',
    }

    return render(request, 'sell.html', context)