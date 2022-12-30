from django.forms import ModelForm
from parking.models import Reservation
from datetime import datetime


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        format = "%H:%M:%S"
        start = cleaned_data['checkin'].strftime(format)
        end =   cleaned_data['checkout'].strftime(format)
        # Get interval between two timstamps as timedelta object
        diff = datetime.strptime(end, format) - datetime.strptime(start, format)
        # Get interval between two timstamps in hours
        duration_in_s = diff.total_seconds()

        hours = divmod(duration_in_s, 3600)[0]

        if hours < 1:
            msg = "Checkout must be at least 1 hour more than checkin."
            self.add_error('checkout', msg)
