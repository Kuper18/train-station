from rest_framework import serializers

from railway.models.train_type import TrainType


class TrainTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainType
        fields = ("id", "name")
        read_only_fields = ("id",)
