from django.forms import ModelForm
from parking.models import Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"
