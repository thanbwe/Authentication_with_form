# forms.py
from django import forms
from .models import Coffee

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ['name', 'price', 'qty', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter coffee name'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price',
                'step': '0.01'
            }),
            'qty': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter quantity'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

