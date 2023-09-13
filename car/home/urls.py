from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import *

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('home',views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('buy',views.buy, name='buy'),
    path('sell',views.sell, name='sell'),

]