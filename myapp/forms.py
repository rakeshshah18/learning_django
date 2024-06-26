from django import forms


shifts = [
    ("1", 'Morning'),
    ("2", 'Afternoon'),
    ("3", 'Evening'),
]

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    shifts = forms.ChoiceField(choices=shifts)
    time_log = forms.TimeField()