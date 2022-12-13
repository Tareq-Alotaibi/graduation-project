from django.contrib import admin
from django.urls import path
from parking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name="home"),
    path('reserve/', views.BookingView.as_view(), name="booking"),
]
