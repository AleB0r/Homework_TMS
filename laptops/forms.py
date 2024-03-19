from django import forms

from laptops.models import Laptop


class AddLaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ['name', 'manufacturer', 'price']
        