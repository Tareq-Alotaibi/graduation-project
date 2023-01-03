from django.http import JsonResponse
from parking.models import Reservation, Parking
from datetime import datetime


def get_available(request):
    now = datetime.now()
    off_parkings = Parking.objects.filter(
        reservations__date=now.date(), 
        reservations__checkin__lte=now.time(), 
        reservations__checkout__gt=now.time(),
    )

    response = {}

    for parking in Parking.objects.all():
        response[parking.name] = 0 if parking in off_parkings else 1

    return JsonResponse(response, safe=False)
