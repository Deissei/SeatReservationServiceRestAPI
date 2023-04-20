from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Event, Seat, Reservation
from .serializers import EventSerializer, SeatSerializer, ReservationSerializer

from rest_framework.serializers import ValidationError

class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class SeatList(generics.ListAPIView):
    serializer_class = SeatSerializer

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return Seat.objects.filter(event_id=event_id)


class ReservationCreate(generics.CreateAPIView):
    # queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        seat_id = self.request.data.get('seat_id')
        seat = Seat.objects.select_for_update().get(id=seat_id)
        if seat.is_reserved:
            raise ValidationError('This seat has already been reserved.')
        seat.is_reserved = True
        seat.save()
        serializer.save(user=user, seat=seat)