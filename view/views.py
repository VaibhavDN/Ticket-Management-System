from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from book.models import TicketInfo
from .serializer import TicketInfoSerializer
from rest_framework.response import Response
import json
from django.http import JsonResponse

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST', ])
def viewTicketDetails(request):
    try:
        data = request.body
        json_data = json.loads(data.decode('utf-8'))
        query = json_data['query']
        ticketInfo = {}

        if(query == 'all'):
            ticketInfo = TicketInfo.objects.all()
        elif(query == 'id'):
            id = json_data['id']
            ticketInfo = TicketInfo.objects.filter(ticketId = id)
        elif(query == 'datetime'):
            _date = 'NA'
            try:
                _date = json_data['date']
            except:
                print("No date found")

            _timeList = []
            try:
                _time_raw = json_data['time']
                _timeList = _time_raw.split(":")
            except:
                print("No time specified")

            _hours = 0
            _minutes = 0
            _seconds = 0

            #* If hours minutes and seconds are available
            if(len(_timeList) == 3):
                _hours = _timeList[0]
                _minutes = _timeList[1]
                _seconds = _timeList[2]
                if(_date != 'NA'):
                    ticketInfo = TicketInfo.objects.filter(date = _date).filter(time_hours = _hours).filter(time_minutes = _minutes).filter(time_seconds = _seconds)
                else:    
                    ticketInfo = TicketInfo.objects.filter(time_hours = _hours).filter(time_minutes = _minutes).filter(time_seconds = _seconds)
            #* If hours and minutes are available
            elif(len(_timeList) == 2):
                _hours = _timeList[0]
                _minutes = _timeList[1]
                if(_date != 'NA'):
                    ticketInfo = TicketInfo.objects.filter(date = _date).filter(time_hours = _hours).filter(time_minutes = _minutes)
                else:
                    ticketInfo = TicketInfo.objects.filter(time_hours = _hours).filter(time_minutes = _minutes)
            #* If only hours are available
            elif(len(_timeList) == 1):
                _hours = _timeList[0]
                if(_date != 'NA'):
                    ticketInfo = TicketInfo.objects.filter(date = _date).filter(time_hours = _hours)
                else:
                    ticketInfo = TicketInfo.objects.filter(time_hours = _hours)
            elif(_date != 'NA'):
                ticketInfo = TicketInfo.objects.filter(date = _date)
        else:
            raise("Invalid query")

        #* End of select conditions
        if (len(ticketInfo) > 0):
            ticket = TicketInfoSerializer(ticketInfo, many=True)
            return Response(ticket.data)
        else:
            return JsonResponse({'status': False, 'message': "Record not found"})
    except:
        return HttpResponse("Invalid request. Please send a valid POST request.")