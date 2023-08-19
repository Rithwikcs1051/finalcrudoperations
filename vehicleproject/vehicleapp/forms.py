from django import forms

from vehicleapp.models import cars

from vehicleapp.models import bikes


class carsform(forms.ModelForm):
    class Meta:
        model=cars
        fields='__all__'
class bikesform(forms.ModelForm):
    class Meta:
        model=bikes
        fields='__all__'