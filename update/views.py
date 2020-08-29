from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from book.models import TicketInfo
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def editTicket(request):
    try:
        data = request.body
        json_data = json.loads(data.decode('utf-8'))

        #! If id is not provided no modifications can be performed
        if 'id' not in json_data:
            raise('Invalid request')

        id = json_data['id']

        #* Init
        ticketQuerySet = TicketInfo.objects.filter(ticketId = id)
        if (len(ticketQuerySet) == 0):
            raise Exception('Id not found')

        ticketInfo = ticketQuerySet[0]
        #* Fields modification received
        if 'firstname' in json_data:
            ticketInfo.firstname = json_data['firstname']

        if 'lastname' in json_data:
            ticketInfo.lastname = json_data['lastname']

        if 'phone_number' in json_data:
            phno = str(json_data['phone_number'])
            if(len(phno) != 10):
                raise Exception('Phone number must be of 10 digits')

            ticketInfo.phone_number = json_data['phone_number']

        if 'date' in json_data:
            _date = json_data['date']
            _date = _date.split('-')
            if(len(_date) != 3):
                raise Exception('Incorrect date format. Should be dd-mm-yyyy')

            if(_date[0].isnumeric() and _date[1].isnumeric() and _date[2].isnumeric()):
                ticketInfo.date = json_data['date']
            else:
                raise Exception('Incorrect date format. Should be dd-mm-yyyy')

        if 'time' in json_data:
            _time = json_data['time']
            _timeList = _time.split(':')

            #* Time list length
            _timeListLen = len(_timeList)

            #* Time format 3:15:26
            if(_timeListLen == 3):
                if(_timeList[0].isnumeric() and _timeList[1].isnumeric() and _timeList[2].isnumeric()):
                    ticketInfo.time_hours = _timeList[0]
                    ticketInfo.time_minutes = _timeList[1]
                    ticketInfo.time_seconds = _timeList[2]
                else:
                    raise Exception('Incorrect time format')
            #* Time format 3:15
            elif(_timeListLen == 2):
                if(_timeList[0].isnumeric() and _timeList[1].isnumeric()):
                    ticketInfo.time_hours = _timeList[0]
                    ticketInfo.time_minutes = _timeList[1]
                else:
                    raise Exception('Incorrect time format')
            #* Time format 3
            elif(_timeListLen == 1):
                if(_timeList[0].isnumeric()):
                    ticketInfo.time_hours = _timeList[0]
                else:
                    raise Exception('Incorrect time format')
            else:
                raise Exception('Incorrect time format')

        saved = ticketInfo.save()
        return JsonResponse({'status': True, 'message': 'Success'})

    except Exception as e:
        return JsonResponse({'status': False, 'message': str(e)})


@csrf_exempt
@api_view(['GET', 'POST'])
def deleteTicket(request):
    try:
        data = request.body
        json_data = json.loads(data.decode('utf-8'))

        #! If id is not provided deletion can't be done
        if 'id' not in json_data:
            raise('Invalid request')

        id = json_data['id']

        ticketQuerySet = TicketInfo.objects.filter(ticketId = id)
        if(len(ticketQuerySet) == 0):
            raise Exception("Id not found")

        ticketInfo = ticketQuerySet[0]
        ticketInfo.delete()

        return JsonResponse({'status': True, 'message': 'Success'})

    except Exception as e:
        return JsonResponse({'status': False, 'message': str(e)})