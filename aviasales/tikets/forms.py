from .models import *
from django import forms
from django.contrib.admin import widgets


    # Принимаемые атрибуты
    # required=True/False - обязательное поле или нет
    # initial='изначальное значение'
    # empty_label='(Nothing)' - изначальное значение выпадающих списков. если NONE то первый элемент
    # widget - все что хотим применить к инпуту

class FormFindTiket(forms.Form):

    # departure_place = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control mb-2 mr-sm-2',
    #             'placeholder': 'Откуда',
    #         }
    #     ),
    # )

    city_query = Airport.objects.all()
    city_array = []
    for key in city_query:
        city = key.city
        city_array.append([city, city])

    departure_place = forms.ChoiceField(
        widget=forms.Select(
           attrs={
               'class':"selectpicker show-tick form-control",
               'data-live-search':"true",
               'id':"basic",
           }
        ),
        choices=city_array,
        required=True,
    )

    arrivial_place = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': "selectpicker show-tick form-control",
                'data-live-search': "true",
                'id': "basic",
            }
        ),
        choices=city_array,
        required=True,
    )

    departure_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Когда',
            }
        ),
    )

    departure_date_back = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Когда',
            }
        ),
    )


class PlaceForm(forms.Form):

    class_array = (
        ('Эконом', 'Эконом'),
        ('Бизнесс', 'Бизнесс'),
        ('VIP', 'VIP'),
    )

    place_class = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control-sm',
            }
        ),
        choices=class_array,
        label='Категория места',
        required=True,
    )

    window_place = forms.BooleanField(
        widget=forms.CheckboxInput(),
        label='Место у окна',
        required=False,
    )

    baggage = forms.BooleanField(
        widget=forms.CheckboxInput(),
        label='Наличие багажа',
        required=False,
    )

class BuyForm(forms.Form):

    names = Flights.objects.all()

    surename = forms.CharField(

        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-2 mr-sm-2',
                'placeholder': 'Фамилия',
            }
        ),
    )
    name = forms.CharField(

        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-2 mr-sm-2',
                'placeholder': 'Имя',
            }
        ),
    )
    fathername = forms.CharField(

        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-2 mr-sm-2',
                'placeholder': 'Отчество',
            }
        ),
    )
    phone = forms.IntegerField(

        widget=forms.NumberInput(
            attrs={
                'class': 'form-control mb-2 mr-sm-2',
                'placeholder': '89610000000',
            }
        ),
    )
    pasport = forms.CharField(

        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-2 mr-sm-2',
                'placeholder': 'Серия номер паспорта',
            }
        ),
    )
