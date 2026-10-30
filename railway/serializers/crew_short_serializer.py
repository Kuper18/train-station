from rest_framework import serializers

from railway.models import Crew


class CrewShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ("id", "first_name", "last_name", "full_name")
        read_only_fields = ("id", "full_name")
