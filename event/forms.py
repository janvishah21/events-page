from django import forms
from .widgets import DateTimePickerInput

class CreateEventForm(forms.Form):
    name = forms.CharField(label='Event Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    time = forms.DateTimeField(
    	label='Date and Time',
        input_formats=['%d/%m/%Y %H:%M'],
        widget=DateTimePickerInput()
    )
    location = forms.CharField(label='Event Location', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.FileField(label='Event Image', required=False)