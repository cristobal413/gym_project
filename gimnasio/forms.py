from django import forms
from .models import ImplementoGym

class ImplementoGymForm(forms.ModelForm):
    class Meta:
        model = ImplementoGym
        fields = ['tipo', 'nombre', 'precio', 'fecha_adquisicion', 'disponible']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Mancuerna 10kg'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fecha_adquisicion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }