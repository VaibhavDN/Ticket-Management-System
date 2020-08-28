from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewTicketDetails, name="ViewTicketDetails")
]
