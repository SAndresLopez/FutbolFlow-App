from django import forms
from .models import PerfilJugador
import re

class RegistroPerfilForm(forms.ModelForm):
    DISTRITOS_LIMA = [
        ('Miraflores', 'Miraflores'),
        ('San Isidro', 'San Isidro'),
        ('Santiago de Surco', 'Santiago de Surco'),
        ('La Molina', 'La Molina'),
        ('San Borja', 'San Borja'),
        ('Lince', 'Lince'),
        ('Magdalena del Mar', 'Magdalena del Mar'),
        ('Pueblo Libre', 'Pueblo Libre'),
        ('Jesús María', 'Jesús María'),
        ('San Miguel', 'San Miguel'),
    ]

    distrito = forms.ChoiceField(choices=DISTRITOS_LIMA, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = PerfilJugador
        fields = ['apodo', 'telefono', 'distrito', 'posicion']

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        if len(telefono) < 9:
            raise forms.ValidationError("El teléfono debe tener al menos 9 dígitos.")
        return telefono