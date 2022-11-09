from django.db import models
from enum import Enum
# Create your models here.

time_slots = [
    ('Time1', '09:00 – 10:00'),
    ('Time2', '10:00 – 11:00'), 
    ('Time3', '11:00 – 12:00'), 
    ('Time4', '12:00 – 13:00'), 
    ('Time5', '13:00 – 14:00'), 
    ('Time6', '14:00 – 15:00'), 
    ('Time7', '15:00 – 16:00'), 
    ('Time8', '16:00 – 17:00')
]


class Parking(models.Model):
    name = models.CharField(max_length=255, null=True)
    number = models.IntegerField(null=True, unique=True)
    is_available = models.BooleanField(default=True, null=True)

    def __str__(self) -> str:
        return f"Parking number {str(self.number)}"


class Reservation(models.Model):

    parking = models.ForeignKey(Parking, on_delete=models.DO_NOTHING)
    car_number = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(null=True, max_length=60)
    date = models.DateField(null=True, blank=True)
    checkin = models.TimeField(null=True, blank=True)
    checkout = models.TimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Car number {self.car_number}, {self.parking}"