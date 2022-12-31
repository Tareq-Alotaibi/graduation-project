from django.db import models
# Create your models here.


class Parking(models.Model):
    name = models.CharField(max_length=255, null=True)
    number = models.IntegerField(null=True, unique=True)
    is_available = models.BooleanField(default=True, null=True)

    def __str__(self) -> str:
        return f"Parking number {str(self.number)}"


class Reservation(models.Model):

    parking = models.ForeignKey(Parking, on_delete=models.DO_NOTHING, related_name="reservations")
    car_number = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(null=True, max_length=60)
    date = models.DateField(null=True, blank=True)
    checkin = models.TimeField(null=True, blank=True)
    checkout = models.TimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Car number {self.car_number}, {self.parking}"