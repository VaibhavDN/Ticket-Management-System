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
    #print(request.body)
    if not request.GET:
        try:
            body_content = request.body.decode('utf-8')
            json_data = json.loads(body_content)

            #* Check if all the required information is available
            required = ['firstname', 'lastname', 'phone_number', 'date', 'time']
            for key in required:
                if(key not in json_data):
                    raise Exception('Missing required parameters')

            #* Extracting information
            _firstname = json_data['firstname']
            _lastname = json_data['lastname']
            _phone_number = json_data['phone_number']
            phno = str(_phone_number)
            if(len(phno) != 10):
                raise Exception('Phone number must be of 10 digits')

            _date = json_data['date']
            _dateList = _date.split('-')
            if(len(_dateList) != 3):
                raise Exception('Incorrect date format. Should be dd-mm-yyyy')

            if(not (_dateList[0].isnumeric() and _dateList[1].isnumeric() and _dateList[2].isnumeric())):
                raise Exception('Incorrect date format. Should be dd-mm-yyyy')
            
            _hours = 0
            _minutes = 0
            _seconds = 0

            _time = json_data['time']
            _timeList = _time.split(':')

            #* Time list length
            _timeListLen = len(_timeList)

            #* Time format 3:15:26
            if(_timeListLen == 3):
                if(not (_timeList[0].isnumeric() and _timeList[1].isnumeric() and _timeList[2].isnumeric())):
                    raise Exception('Incorrect time format')
                _hours = _timeList[0]
                _minutes = _timeList[1]
                _seconds = _timeList[2]

            #* Time format 3:15
            elif(_timeListLen == 2):
                if(not (_timeList[0].isnumeric() and _timeList[1].isnumeric())):
                    raise Exception('Incorrect time format')
                _hours = _timeList[0]
                _minutes = _timeList[1]
            
            #* Time format 3
            elif(_timeListLen == 1):
                if(not (_timeList[0].isnumeric())):
                    raise Exception('Incorrect time format')
                _hours = _timeList[0]

            else:
                raise Exception('Incorrect time format')

            #************************

            ticketsInfo = TicketInfo()

            #* Check if more than 20 entries are already present
            count = TicketInfo.objects.filter(date = _date).filter(time_hours = _hours).filter(time_minutes = _minutes).count()

            if (count > 20):
                return JsonResponse({'status': False, 'message': '20 entries already exist for this time'})

            #* Saving user details
            ticketsInfo.firstname = _firstname
            ticketsInfo.lastname = _lastname
            ticketsInfo.phone_number = _phone_number
            ticketsInfo.date = _date
            ticketsInfo.time_hours = _hours
            ticketsInfo.time_minutes = _minutes
            ticketsInfo.time_seconds = _seconds
            ticketsInfo.expired = False
            ticketsInfo.save()
            saved = ticketsInfo.pk

            return JsonResponse({'status': True, 'message': "Success", 'id': saved})

        except Exception as e:
            return JsonResponse({'status': False, 'message': str(e)})

        return JsonResponse(json_data)
    else:
        return HttpResponse("<center><h2>Please send a post request at http://127.0.0.1:8000/book/</h2></center>")
