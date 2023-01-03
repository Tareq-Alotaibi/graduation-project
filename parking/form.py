from django.forms import ModelForm
from parking.models import Reservation
from datetime import datetime
from datetime import timedelta
from django.db.models import Q


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"

    def validate_time_over(self, cleaned_data):
        now = datetime.now()
        if cleaned_data['date'] < now.date() or cleaned_data['checkout'] < now.time():
            msg = "Time is over."
            self.add_error('checkout', msg)
            return False

        return True


    def validate_checkout_gt_checkin(self, cleaned_data):
        format = "%I:%M %p"

        start = cleaned_data['checkin'].strftime(format)
        end =   cleaned_data['checkout'].strftime(format)
        
        date_start = datetime.strptime(start, format)
        date_end = datetime.strptime(end, format)

        if cleaned_data['checkout'] < cleaned_data['checkin']:
            date_end = datetime.strptime(end, format) + timedelta(days=1)

        diff = date_end - date_start
        duration_in_s = diff.total_seconds()

        hours = duration_in_s / (60 * 60)

        if hours < 1:
            msg = "Checkout must be at least 1 hour more than checkin."
            self.add_error('checkout', msg)
            return False

        return True

    def validate_overlapping(self, cleaned_data):
        reservations = Reservation.objects.filter(
            Q(parking=cleaned_data['parking'])
            & Q(date=cleaned_data['date']) 
            & Q(
                Q(
                    Q(checkin__lte=cleaned_data['checkin'])
                    & Q(checkout__gt=cleaned_data['checkin'])
                )
                | Q(
                    Q(checkin__lte=cleaned_data['checkin'])
                    & Q(checkout__gt=cleaned_data['checkin'])
                )
                | Q(
                    Q(checkin__gte=cleaned_data['checkin'])
                    & Q(checkout__lte=cleaned_data['checkout'])
                )
            )
        ).exists()

        if reservations:
            msg = "Time is reserved by someone else."
            self.add_error('checkout', msg)
            return False    
        return True

    def clean(self):
        cleaned_data = super().clean()

        valid = self.validate_time_over(cleaned_data)

        if not valid:
            return

        valid = self.validate_checkout_gt_checkin(cleaned_data)
        
        if not valid:
            return

        valid = self.validate_overlapping(cleaned_data)
        if not valid:
            return