import django
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import pytz
import os
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE","TMS.settings")
django.setup()
from book.models import TicketInfo

scheduler = BlockingScheduler()
print("Running..")

@scheduler.scheduled_job('interval', minutes=1)
def timed_job():
    print("Started..")
    ticketQuerySet = TicketInfo.objects.all()
    for ticketInfo in ticketQuerySet:
        date = ticketInfo.date
        dateList = date.split('-')

        hours = int(ticketInfo.time_hours)
        minutes = int(ticketInfo.time_minutes)
        seconds = int(ticketInfo.time_seconds)

        indian_timezone = pytz.timezone('Asia/Calcutta')
        _time = indian_timezone.localize(datetime(int(dateList[2]), int(dateList[1]), int(dateList[0]), hours, minutes, seconds, 0))
        current_time = datetime.now(tz=indian_timezone)

        difference = divmod((_time-current_time).total_seconds(), 3600)[0]
        if(difference < -8):
            print("8 hours old", ticketInfo)
            ticketInfo.expired = True   #Diff of 8 hours between the ticket timing and current time
            ticketInfo.delete() #Delete all the tickets which are expired automatically

    #scheduler.shutdown(wait=False)

scheduler.start()