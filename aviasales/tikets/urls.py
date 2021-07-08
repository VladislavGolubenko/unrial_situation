from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('view_tikets/', scroll, name='view_tikets'),
    path('buy_tiket/<int:id_flight>/', buy_tiket, name='buy_tiket'),
    path('get_contact/<int:id_flight>/', get_contact, name='get_contact'),
    path('map/', russia_map, name='russia_map'),
]