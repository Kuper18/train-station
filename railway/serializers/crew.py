from rest_framework import serializers

from railway.models.crew import Crew
from railway.serializers.trip import TripWithoutCrewSerializer


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ("id", "first_name", "last_name", "full_name", "trips")
        read_only_fields = ("id", "full_name")


class CrewDetailSerializer(CrewSerializer):
    trips = TripWithoutCrewSerializer(many=True, read_only=True)

    class Meta:
        model = Crew
        fields = ("id", "first_name", "last_name", "full_name", "trips")
        read_only_fields = ("id", "full_name")
