from rest_framework import serializers

from railway.models.ticket import Ticket


class TicketListSerializer(serializers.ListSerializer):
    def validate(self, data):
        seen = set()
        for item in data:
            identifier = (item.get("car"), item.get("seat"), item.get("trip"))
            if identifier in seen:
                raise serializers.ValidationError(
                    "Duplicate tickets found in the booking request."
                )
            seen.add(identifier)
        return super().validate(data)


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            "id",
            "seat",
            "car",
            "trip",
        )
        read_only_fields = ("id",)
        list_serializer_class = TicketListSerializer

    def validate(self, attr):
        data = super(TicketSerializer, self).validate(attr)

        Ticket.validate_seat(
            seat=attr["seat"],
            num_seats=attr["trip"].train.places_per_car,
            car=attr["car"],
            car_count=attr["trip"].train.car_count,
            error_to_raise=serializers.ValidationError,
        )

        return data
