from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login


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


def buy2(request):
    cars = car.objects.filter(is_sold=False)
    categories = category.objects.all
    category_id = request.GET.get('category', 0)
    brand_id = request.GET.get('brand', 0)
    engine_capacity_id = request.GET.get('engine_capacity', 0)
    brands = brand.objects.all
    engine = engine_capacity.objects.all
    query = request.GET.get('query', '')

    if category_id:
        cars = cars.filter(category_id=category_id)


    if brand_id:
        cars = cars.filter(brand_id=brand_id)

    if engine_capacity_id:
        cars = cars.filter(engine_capacity_id=engine_capacity_id)

    if query:
        cars = cars.filter(name__icontains=query) | Q(description__icontains=query)

    context = {
        'cars':cars,
        'query':query,
        'categories':categories,
        'brands':brands,
        'engine':engine,
        'category_id':int(category_id),
        'brand_id':int(brand_id),
        'engine_capacity_id':int(engine_capacity_id),


        
        
    }

    return render(request, 'buy2.html', context)
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




     