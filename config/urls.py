from django.contrib import admin
from django.urls import path
from parking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', views.BookingView.as_view(), name="book"),
]
