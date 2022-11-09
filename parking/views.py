from django.shortcuts import redirect, render
from django.views import View
from parking.form import ReservationForm

from parking.models import Parking
# Create your views here.


class BookingView(View):

    def get(self, request):
        parkings = Parking.objects.all()

        context = {
            "parkings": parkings,
        }

        return render(request, "parking/book.html", context)

    def post(self, request):
        get = request.POST.get

        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("book")