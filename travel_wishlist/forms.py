from django import forms
from django.forms import DateInput
from .models import Place


#This ties together the form object with the model object so that django knows how they relate
class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited')

# class DateInput(forms.DateInput):
#     input_type = 'date'

class DateInput(forms.DateInput):
    input_type = 'date'

class TripReviewForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('notes', 'date_visited', 'photo')
        widgets = {
            'date_visited': DateInput()
        }
