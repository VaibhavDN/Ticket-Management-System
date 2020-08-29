from django.urls import path
from . import views

urlpatterns = [
    path('edit/', views.editTicket, name="EditTicket"),
    path('delete/', views.deleteTicket, name="DeleteTicket")
]