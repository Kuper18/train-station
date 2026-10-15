from rest_framework import viewsets

from station.models.train import Train
from station.models.train_type import TrainType
from station.serializers.train import (
    TrainDetailSerializer,
    TrainListSerializer,
    TrainSerializer,
)
from station.serializers.train_type import TrainTypeSerializer


class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.select_related("train_type")
    serializer_class = TrainSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return TrainListSerializer

        if self.action == "retrieve":
            return TrainDetailSerializer

        return TrainSerializer


class TrainTypeViewSet(viewsets.ModelViewSet):
    queryset = TrainType.objects.all()
    serializer_class = TrainTypeSerializer
