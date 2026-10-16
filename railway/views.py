from rest_framework import viewsets

from railway.models import Crew
from railway.models.route import Route
from railway.models.station import Station
from railway.models.train import Train
from railway.models.train_type import TrainType
from railway.models.trip import Trip
from railway.serializers.crew import CrewDetailSerializer, CrewSerializer
from railway.serializers.crew_short_serializer import CrewShortSerializer
from railway.serializers.route import (
    RouteDetailSerializer,
    RouteListSerializer,
    RouteSerializer,
)
from railway.serializers.station import StationSerializer
from railway.serializers.train import (
    TrainDetailSerializer,
    TrainListSerializer,
    TrainSerializer,
)
from railway.serializers.train_type import TrainTypeSerializer
from railway.serializers.trip import (
    TripDetailSerializer,
    TripListSerializer,
    TripSerializer,
)


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

        if self.action == "retrieve":
            serializer = RouteDetailSerializer

        return serializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()

    def get_serializer_class(self):
        serializer = TripSerializer

        if self.action == "list":
            serializer = TripListSerializer

        if self.action == "retrieve":
            serializer = TripDetailSerializer

        return serializer

    def get_queryset(self):
        queryset = self.queryset

        if self.action in ("list", "retrieve"):
            queryset = (queryset.select_related(
                "train",
                "route__destination",
                "route__source",
            ).prefetch_related("crews"))

        return queryset


class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()

    def get_serializer_class(self):
        serializer = CrewSerializer

        if self.action == "list":
            serializer = CrewShortSerializer

        if self.action == "retrieve":
            serializer  = CrewDetailSerializer

        return serializer
