from django.shortcuts import render
from django.http import HttpResponse
from .filters import FlightFilter
from .forms import FormFindTiket, PlaceForm, BuyForm
from .models import *
import datetime
from datetime import timedelta

def index(request):

    form = FormFindTiket()

    context = {
        'form': form,
    }

    return render(request, 'tikets/find_page.html', context=context)


def scroll(request):
    region = request.GET.get("region", "")

    if region != "":
        date = datetime.datetime.now()
        flights = Flights.objects.select_related('arrival_point_airport').filter(arrival_point_airport__country=region,
                                                                                 departure_time__gte=date,
                                                                                 departure_airport__city='Ростов-на-Дону')

        filter = FlightFilter(request.GET, queryset=flights)

        carrier = Carrier.objects.all()

        form = FormFindTiket()

        context = {
            'flights': flights,
            'title': 'Отображение',
            'carriers': carrier,
            'filter': filter,
            'form': form,
        }

        return render(request, 'tikets/scroll.html', context=context)

    if request.method == 'POST':

        form = FormFindTiket(request.POST)

        if form.is_valid() and form.is_bound:

            airport_query = Airport.objects.all()

            departure_place = form.cleaned_data['departure_place']
            arrivial_place = form.cleaned_data['arrivial_place']
            departure_date = form.cleaned_data['departure_date']
            departure_date_back_min = form.cleaned_data['departure_date_back']
            departure_date_back_max = departure_date_back_min + timedelta(days=1)

            departure_date = str(departure_date)
            departure_date_back_max = str(departure_date_back_max)
            departure_date_back_min = str(departure_date_back_min)

            request.session['departure_date'] = departure_date
            request.session['departure_place'] = departure_place
            request.session['arrivial_place'] = arrivial_place
            request.session['departure_date_back_max'] = departure_date_back_max
            request.session['departure_date_back_min'] = departure_date_back_min

            for airport in airport_query:
                if departure_place == airport.city:
                    departure_place_id = airport.pk
                    request.session['departure_place_id'] = departure_place_id

                if arrivial_place == airport.city:
                    arrivial_place_id = airport.pk
                    request.session['arrivial_place_id'] = arrivial_place_id



    form = FormFindTiket()

    departure_date = request.session.get('departure_date')
    departure_place_id = request.session.get('departure_place_id')
    arrivial_place_id = request.session.get('arrivial_place_id')

    departure_date_back_max = request.session.get('departure_date_back_max')
    departure_date_back_min = request.session.get('departure_date_back_min')
    print(departure_date_back_min, departure_date_back_max, arrivial_place_id, departure_place_id)

    flights_back = Flights.objects.filter(departure_airport=arrivial_place_id, arrival_point_airport=departure_place_id).filter(departure_time__date=departure_date_back_min).order_by('departure_time')

    flights = Flights.objects.filter(departure_airport=departure_place_id, arrival_point_airport=arrivial_place_id, departure_time__gte=departure_date).order_by('departure_time')
    print(flights)



    filter = FlightFilter(request.GET, queryset=flights)

    carrier = Carrier.objects.all()

    context = {
        'flights': flights,
        'flights_back': flights_back,
        'title': 'Отображение',
        'carriers': carrier,
        'filter': filter,
        'form': form,
    }

    return render(request, 'tikets/scroll.html', context=context)

def buy_tiket(request, id_flight):

    form = PlaceForm()

    flights = Flights.objects.filter(id=id_flight)

    context = {
        'flights': flights,
        'form': form,
        'id_flight': id_flight,
        'flights': flights,
    }

    return render(request, 'tikets/buy_tiket.html', context=context)

def get_contact(request, id_flight):

    if request.method == 'POST':
        form_place = PlaceForm(request.POST)

        if form_place.is_valid() and form_place.is_bound:

            place_class = form_place.cleaned_data['place_class']
            window_place = form_place.cleaned_data['window_place']
            baggage = form_place.cleaned_data['baggage']
            request.session['place_class'] = place_class
            request.session['window_place'] = window_place
            request.session['baggage'] = baggage

        form_contact = BuyForm(request.POST)

        if form_contact.is_valid() and form_contact.is_bound:

            place_class = request.session.get('place_class')
            window_place = request.session.get('window_place')
            baggage = request.session.get('baggage')

            name = form_contact.cleaned_data['name']
            surename = form_contact.cleaned_data['surename']
            fathername = form_contact.cleaned_data['fathername']
            phone = form_contact.cleaned_data['phone']
            pasport = form_contact.cleaned_data['pasport']

            order = Order(name=name, surename=surename, fathername=fathername, pasport=pasport, phone=phone, place_class=place_class, window_place=window_place, baggage=baggage)
            order.save(force_insert=True)

    else:
        form_contact = BuyForm()

    flights = Flights.objects.filter(id=id_flight)

    place_class = request.session.get('place_class')
    window_place = request.session.get('window_place')
    baggage = request.session.get('baggage')


    context = {
        'form': form_contact,
        'flights': flights,
        'place_class': place_class,
        'window_place': window_place,
        'baggage': baggage,
    }

    return render(request, 'tikets/get_contact.html', context=context)

def russia_map(request):

    return render(request, 'tikets/map.html')


# Возможно понадобится get_object_or_404(News, pk)

