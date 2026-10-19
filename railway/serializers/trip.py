from rest_framework import serializers

from railway.models.route import Route
from railway.models.train import Train
from railway.models.trip import Trip
from railway.serializers.crew_short_serializer import CrewShortSerializer
from railway.serializers.route import RouteListSerializer
from railway.serializers.train import TrainListSerializer, TrainSerializer


class TripSerializer(serializers.ModelSerializer):
    train = serializers.PrimaryKeyRelatedField(
        queryset=Train.objects.select_related("train_type")
    )
    route = serializers.PrimaryKeyRelatedField(
        queryset=Route.objects.select_related("source", "destination")
    )

    class Meta:
        model = Trip
        fields = ("id", "departure_time", "arrival_time", "train", "route", "crews")
        read_only_fields = ("id",)


class TripListSerializer(TripSerializer):
    train = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name"
    )
    crews = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="full_name"
    )
    route = serializers.SerializerMethodField()
    sold_tickets = serializers.IntegerField(
        read_only=True,
    )
    tickets_available = serializers.IntegerField(
        read_only=True,
    )

    def get_route(self, obj):
        return f"{obj.route.source.name} - {obj.route.destination.name}"

    class Meta:
        model = Trip
        fields = (
            "id",
            "departure_time",
            "arrival_time",
            "train",
            "route",
            "crews",
            "sold_tickets",
            "tickets_available",
        )
        read_only_fields = ("id",)


class TripWithoutCrewSerializer(TripListSerializer):
    class Meta:
        model = Trip
        fields = ("id", "departure_time", "arrival_time", "train", "route")


class TripDetailSerializer(TripListSerializer):
    train = TrainListSerializer(many=False)
    crews = CrewShortSerializer(many=True)
    route = RouteListSerializer(many=False)
