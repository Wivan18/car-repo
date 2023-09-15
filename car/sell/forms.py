from django import forms

from .models import car

class NewCarForm(forms.ModelForm):
    class Meta:
        model = car
        fields = ('category', 'name', 'description', 'price', 'image',)