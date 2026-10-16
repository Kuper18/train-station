from rest_framework import serializers

from railway.models.crew import Crew


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ("id", "first_name", "last_name", "full_name", "trips")
        read_only_fields = ("id", "full_name")
