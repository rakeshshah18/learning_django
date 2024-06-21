from django import forms
from django.forms.widgets import NumberInput

class DemoForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(label='Your age')
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
