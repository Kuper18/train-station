from rest_framework import viewsets

from station.models.train import Train
from station.models.train_type import TrainType
from station.serializers.train import TrainListSerializer, TrainSerializer
from station.serializers.train_type import TrainTypeSerializer


class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return TrainListSerializer

        return TrainSerializer


class TrainTypeViewSet(viewsets.ModelViewSet):
    queryset = TrainType.objects.all()
    serializer_class = TrainTypeSerializer
