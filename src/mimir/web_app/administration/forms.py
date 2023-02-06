from django import forms

from shared.value_objects.listing_service.listings import PropertyType

AREA = [
    (5, "< 5 km"),
    (10, "10 km"),
    (20, "20 km"),
    (40, "40 km"),
    (50, "> 50 km"),
]


class ScraperForm(forms.Form):
    property_type = forms.TypedChoiceField(choices=PropertyType)
    city = forms.CharField(max_length=100)
    area = forms.CharField(required=True, label="Range area:", widget=forms.Select(choices=AREA))
    min_price = forms.CharField(max_length=20)
    max_price = forms.CharField(max_length=20)
