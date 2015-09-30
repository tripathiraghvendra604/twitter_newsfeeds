from django import forms
from .models import Country


class CountryForm(forms.Form):
    country = forms.ChoiceField(
        choices=[(country.code, country.name)
                 for country in Country.objects.all()]
    )