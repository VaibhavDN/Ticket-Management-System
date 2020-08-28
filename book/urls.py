from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookTicket, name="BookTicket")
]
