from django import forms
from .models import Laptop, Processor, VideoCard

class AddLaptopForm(forms.ModelForm):
    processor = forms.ModelChoiceField(queryset=Processor.objects.all())
    video_card = forms.ModelChoiceField(queryset=VideoCard.objects.all())

    class Meta:
        model = Laptop
        fields = ['name', 'manufacturer', 'price', 'processor', 'video_card']

class EditLaptopForm(forms.ModelForm):
    processor = forms.ModelChoiceField(queryset=Processor.objects.all())
    video_card = forms.ModelChoiceField(queryset=VideoCard.objects.all())

    class Meta:
        model = Laptop
        fields = ['name', 'manufacturer', 'price', 'processor', 'video_card']
