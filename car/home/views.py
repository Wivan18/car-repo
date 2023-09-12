from django.shortcuts import render,redirect
from sell.models import category,car

def index(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')
def buy(request):
    return render(request, 'buy.html')
    
def sell(request):
    return render(request, 'sell.html')