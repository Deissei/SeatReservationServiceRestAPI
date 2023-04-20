from rest_framework import serializers
from .models import Event, Seat, Reservation

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'venue')

class SeatSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = Seat
        fields = ('id', 'event', 'row', 'number', 'price', 'is_reserved')

class ReservationSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    seat = SeatSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = ('id', 'event', 'seat', 'user', 'timestamp')