from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventList.as_view(), name='event-list'),
    path('events/<int:event_id>/seats/', views.SeatList.as_view(), name='seat-list'),
    path('reservations/', views.ReservationCreate.as_view(), name='reservation-create'),
]