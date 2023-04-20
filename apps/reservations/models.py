from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Seat(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    row = models.CharField(max_length=10)
    number = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return self.event.name

class Reservation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -> {self.event}"
