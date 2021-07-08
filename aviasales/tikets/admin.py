from django.contrib import admin

from .models import *

class AirportAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'city', 'airport_name', 'airport_code', 'adress', 'contact_phone')
    list_display_links = ('id', 'airport_code')  # какие поля будут ссылками
    search_fields = ('airport_name', 'airport_code')  # по каким полям будет происходить поиск
    # list_editable = ('contact_phone',)  # какие поля можно редактировать сразу в таблице
    # list_filter = ('airport_name',)  # для вывода боковых фильтров вывода

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'surename', 'name', 'fathername', 'pasport', 'phone')
    list_display_links = ('id', 'surename')
    search_fields = ('surename', 'pasport', 'phone')

class CarrierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_phone', 'adress', 'logo')
    list_display_links = ('id', 'name')
    search_field = ('name')

class PlaneAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_plane', 'places', 'vip_places',  'bussines_places',  'econom',  'carrier_id')
    list_display_links = ('id', 'model_plane')
    search_field = ('model_plane')

class TiketAdmin(admin.ModelAdmin):
    list_display = ('id', 'flight_id', 'order_id', 'place', 'purchase_date', 'depatrure_date', 'trunk')

class FlightsAdmin(admin.ModelAdmin):
    list_display = ('id', 'departure_airport', 'arrival_point_airport', 'transfer_point', 'departure_time', 'arrival_time', 'plane_id', 'vip_price', 'bussines_price', 'econom_price', 'window_upsale', 'trunk_sale')
    list_editable = ('vip_price', 'bussines_price', 'econom_price', 'window_upsale', 'trunk_sale')

admin.site.register(Flights, FlightsAdmin)
admin.site.register(Airport, AirportAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Carrier, CarrierAdmin)
admin.site.register(Plane, PlaneAdmin)
admin.site.register(Tiket, TiketAdmin)


