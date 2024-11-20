from django import forms
from .models import Place

#This ties together the form object with the model object so that django knows how they relate
class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited')
