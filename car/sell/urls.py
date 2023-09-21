from django.urls import path

from . import views

app_name = 'sell'

urlpatterns = [
    path('new', views.sell, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    ]