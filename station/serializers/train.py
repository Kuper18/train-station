from rest_framework import serializers

from station.models.train import Train
from station.serializers.train_type import TrainTypeSerializer


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = (
            "id",
            "name",
            "car_count",
            "places_per_car",
            "train_type",
            "total_seats",
        )
        read_only_fields = ("id", "total_seats")


class TrainListSerializer(TrainSerializer):
    train_type = serializers.SlugRelatedField(
        slug_field="name",
        read_only=True,
    )


class TrainDetailSerializer(TrainSerializer):
    train_type = TrainTypeSerializer(many=False, read_only=True)
