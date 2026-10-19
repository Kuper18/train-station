from django.db import transaction
from rest_framework import serializers

from railway.models.order import Order
from railway.models.ticket import Ticket
from railway.serializers.ticket import TicketSerializer


class OrderSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=False, allow_empty=False)

    class Meta:
        model = Order
        fields = ("id", "created_at", "tickets")
        read_only_fields = ("id", "created_at")

    @transaction.atomic
    def create(self, validated_data):
        tickets = validated_data.pop("tickets")
        order = Order.objects.create(**validated_data)

        for ticket in tickets:
            Ticket.objects.create(order=order, **ticket)

        return order
