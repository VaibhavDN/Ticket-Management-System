from rest_framework import serializers
from book.models import TicketInfo

class TicketInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketInfo
        fields = '__all__'