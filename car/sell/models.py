from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    name = models.CharField('Category Name', max_length=40)
    #description = models.TextField('Description of the car size',null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class brand(models.Model):
    name = models.CharField('Category Name', max_length=40)
    image = models.ImageField(upload_to='carbrands2', null=False)
    #description = models.TextField('Description of the car size',null=True)

    def __str__(self):
        return self.name
    

class engine_capacity(models.Model):
    name = models.IntegerField('Engine Capacity', max_length=40)
       #description = models.TextField('Description of the car size',null=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Engine Capacity'
    def __str__(self):
        return str(self.name)
    

class car(models.Model):
    name = models.CharField('Name of the car', max_length=250)
    category = models.ForeignKey(category, related_name='cars', on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(brand,related_name='cars', on_delete=models.CASCADE, null=True)
    engine_capacity = models.ForeignKey(engine_capacity,related_name='cars', on_delete=models.CASCADE, null=True)
    description = models.TextField('Description of the car:')
    price = models.FloatField('Price')
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='Item', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='car_images', null=False)
    def __str__(self):
       return self.name
    





