from django import forms
from django.forms.widgets import NumberInput

favorite_dish = [
    ('', 'Select your favorite dish'),
    ('Pizza', 'Pizza'),
    ('Burger', 'Burger'),
    ('Pasta', 'Pasta'),
    ('Salad', 'Salad'),
    ('Ice Cream', 'Ice Cream'),
    ('Others', 'Others')

]

class DemoForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(label='Your age')
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    dish = forms.ChoiceField(widget=forms.RadioSelect, choices=favorite_dish)
    # if we remove the widget=forms.RadioSelect, the choices will be displayed as a dropdown menu