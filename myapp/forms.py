from django import forms


shifts = [
    ("1", 'Morning'),
    ("2", 'Afternoon'),
    ("3", 'Evening'),
]

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder':'first name'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder':'last name'}))
    shifts = forms.ChoiceField(choices=shifts)
    time_log = forms.TimeField( widget=forms.TimeInput(attrs={'placeholder':'time log'}), help_text="Enter exact time")