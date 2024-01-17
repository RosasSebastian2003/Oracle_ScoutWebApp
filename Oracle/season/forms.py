from django import forms

class UpdateCountryForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    country_name = forms.CharField(max_length=100)