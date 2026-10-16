from rest_framework import serializers

from railway.models.route import Route
from railway.models.train import Train
from railway.models.trip import Trip


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

    def get_route(self, obj):
        return f"{obj.route.source.name} - {obj.route.destination.name}"

    class Meta:
        model = Trip
        fields = ("id", "departure_time", "arrival_time", "train", "route", "crews")
