from django.forms import ModelForm
from parking.models import Reservation
from datetime import datetime
from datetime import timedelta


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        format = "%I:%M %p"

        start = cleaned_data['checkin'].strftime(format)
        end =   cleaned_data['checkout'].strftime(format)
        
        date_start = datetime.strptime(start, format)
        date_end = datetime.strptime(end, format)

        if 0 <= cleaned_data['checkout'].hour < 12:
            date_end = datetime.strptime(end, format) + timedelta(days=1)
        
        # Get interval between two timstamps as timedelta object
        diff = date_end - date_start
        # Get interval between two timstamps in hours
        duration_in_s = diff.total_seconds()

        hours = duration_in_s / (60 * 60)

        if hours < 1:
            msg = "Checkout must be at least 1 hour more than checkin."
            self.add_error('checkout', msg)
