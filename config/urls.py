from django.contrib import admin
from django.urls import path
from parking import views
from parking import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name="home"),
    path('reserve/', views.BookingView.as_view(), name="booking"),
    path('get-available/', api.get_available, name="get_available_parking"),
]
