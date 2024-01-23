from rest_framework import serializers

from restApi.models import Ticket


class TicketSerializer(serializers.ModelSerializer[Ticket]):
    class Meta:
        model = Ticket
        fields = ["id", "title", "details", "priority", "state", "necessary_tickets"]
