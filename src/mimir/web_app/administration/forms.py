from django import forms

from shared.value_objects.listing_service.listings import PropertyType

AREA = [
    (5, "< 5 miles"),
    (10, "10 miles"),
    (20, "20 miles"),
    (40, "40 miles"),
    (50, "> 50 miles"),
]


class ScraperForm(forms.Form):
    property_type = forms.TypedChoiceField(choices=PropertyType)
    city = forms.CharField(max_length=100)
    area = forms.CharField(required=True, label="Range area:", widget=forms.Select(choices=AREA))
