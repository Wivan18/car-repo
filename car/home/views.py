from django.shortcuts import render,redirect
from sell.models import *
from home.forms import SignupForm, LoginForm



def index(request):
    return render(request, 'base.html')



def home(request):
    cars = car.objects.all()
    brands = brand.objects.all()

    context = {
        'cars':cars,
        'brands':brands,
    }

    return render(request, 'home.html',context)



def buy(request):

    cars = car.objects.all()
    brands = brand.objects.all()

    context = {
        'cars':cars,
        'brands':brands,
    }

    return render(request, 'buy.html',context)
    


def sell(request):
    return render(request, 'sell.html')




def signup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login')
        
    else:
        form = SignupForm

    context = {
        'form':form

    }

    return render (request, 'signup.html',context)
