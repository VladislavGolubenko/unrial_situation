import django_filters
from django import forms
from .models import *



class FlightFilter(django_filters.FilterSet):

    model_query = Plane.objects.all()
    model_array = list()

    for key in model_query:
        model_array.append((key.model_plane, key.model_plane))

    plane_id__model_plane = django_filters.MultipleChoiceFilter(

        widget=forms.CheckboxSelectMultiple(),
        choices=model_array,
    )

    company_query = Carrier.objects.all()
    company_array = list()

    for key in company_query:
        company_array.append((key.name, key.name))

    plane_id__carrier_id__name = django_filters.MultipleChoiceFilter(

        widget=forms.CheckboxSelectMultiple(),
        choices=company_array,
    )



    econom_price = django_filters.RangeFilter()




    class Meta:
        query = Flights.objects.all()
        fields = ['']
