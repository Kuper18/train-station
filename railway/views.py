from rest_framework import viewsets

from railway.models.route import Route
from railway.models.station import Station
from railway.models.train import Train
from railway.models.train_type import TrainType
from railway.serializers.route import RouteListSerializer, RouteSerializer
from railway.serializers.station import StationSerializer
from railway.serializers.train import (
    TrainDetailSerializer,
    TrainListSerializer,
    TrainSerializer,
)
from railway.serializers.train_type import TrainTypeSerializer


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


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.select_related("source", "destination")

    def get_serializer_class(self):
        serializer = RouteSerializer

        if self.action == "list":
            serializer  = RouteListSerializer

        return serializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

