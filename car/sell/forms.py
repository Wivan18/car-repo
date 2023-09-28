from django import forms

from .models import *
INPUT_CLASSES ='w-full py-4 px-3 rounded-xl border w-40px'
class NewCarForm(forms.ModelForm):
    class Meta:
        model = car
        fields = ('category', 'name', 'description', 'price', 'image','brand','engine_capacity')

        widgets = {
            'category':forms.Select(attrs={
                 'class':'w-70px py-2 px-2 rounded-xl border w-20px'
            }),
            'name':forms.TextInput(attrs={
                 'class':'w-100px py-5 px-5 rounded-xl text-black-700 rounded-xl border'
            }),
            'description':forms.Textarea(attrs={
                 'class':'w-full h-20 py-4 px-3 rounded-xl border w-40px'
            }),
            'price':forms.TextInput(attrs={
                 'class':'w-70px py-2 px-2 rounded-xl border w-40px'
            }),
            'image':forms.FileInput(attrs={
                 'class':'w-70px py-2 px-2 rounded-xl border w-40px'
            }),
            'brand':forms.Select(attrs={
               'class':'w-100px py-5 px-5 rounded-xl text-black-700 rounded-xl border'
            }),
            'Engine Capacity':forms.Select(attrs={
               'class':'w-70px py-2 px-2 rounded-xl border w-20px'
            })
            
        }

class EditCarForm(forms.ModelForm):
    class Meta:
        model = car
        fields = ('name', 'description', 'price', 'image','is_sold')

        widgets = {
            'name':forms.TextInput(attrs={
                 'class':INPUT_CLASSES
            }),
            'description':forms.Textarea(attrs={
                 'class':INPUT_CLASSES
            }),
            'price':forms.TextInput(attrs={
                 'class':INPUT_CLASSES
            }),
            'image':forms.FileInput(attrs={
                 'class':INPUT_CLASSES
            }),
        }