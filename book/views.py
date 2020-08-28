from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
import datetime
from .models import TicketInfo

# Create your views here.
@csrf_exempt 
@api_view(['GET', 'POST', ])
def bookTicket(request):
    if not request.GET:
        body_content = request.body.decode('utf-8')
        json_data = json.loads(body_content)

        #* Extracting information

        _firstname = json_data['firstname']
        _lastname = json_data['lastname']
        _phone_number = json_data['phone_number']
        _date = json_data['date']
        _time = json_data['time']
        _time = _time.split(':')
        _hours = _time[0]
        _minutes = _time[1]
        _seconds = _time[2]

        #************************

        ticketsInfo = TicketInfo()

        #* Check if more than 20 entries are already present
        count = TicketInfo.objects.filter(date = _date).filter(time_hours = _hours).filter(time_minutes = _minutes).count()

        if (count > 20):
            return JsonResponse({'status': False, 'message': '20 entries already exist for this time'})

        #* Saving user details
        try:
            ticketsInfo.firstname = _firstname
            ticketsInfo.lastname = _lastname
            ticketsInfo.phone_number = _phone_number
            ticketsInfo.date = _date
            ticketsInfo.time_hours = _hours
            ticketsInfo.time_minutes = _minutes
            ticketsInfo.time_seconds = _seconds
            ticketsInfo.expired = False
            ticketsInfo.save()

            return JsonResponse({'status': True, 'message': "Success"})

        except Exception as e:
            return JsonResponse({'status': False, 'message': str(e)})

        return JsonResponse(json_data)
    else:
        return HttpResponse("<center><h2>Please send a post request at http://127.0.0.1:8000/book/</h2></center>")
