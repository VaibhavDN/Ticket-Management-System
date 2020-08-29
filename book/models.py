from django.db import models
import uuid

# Create your models here.
class TicketInfo(models.Model):
    ticketId = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    firstname = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)
    phone_number = models.IntegerField(default=0)
    #movieName = models.CharField(max_length = 100, default="Unknown")
    date = models.CharField(max_length = 10)
    time_hours = models.IntegerField()
    time_minutes = models.IntegerField(default=0)
    time_seconds = models.IntegerField(default=0)
    expired = models.BooleanField(default=False)

    def __str__(self):
        return "TicketID: " + str(self.ticketId) + " FirstName: " + self.firstname + " LastName: " + self.lastname + " Date: " + self.date + " Time: " + str(self.time_hours)+":"+str(self.time_minutes)+":"+str(self.time_seconds)
