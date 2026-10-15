from rest_framework import serializers

from station.models.train import Train


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = ("id", "name", "car_count", "places_per_car", "train_type")
        read_only_fields = ("id",)
