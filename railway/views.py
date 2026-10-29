from django.db.models import Count, F, Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet

from railway.models import Crew
from railway.models.order import Order
from railway.models.route import Route
from railway.models.station import Station
from railway.models.train import Train
from railway.models.train_type import TrainType
from railway.models.trip import Trip
from railway.serializers.crew import CrewDetailSerializer, CrewSerializer
from railway.serializers.crew_short_serializer import CrewShortSerializer
from railway.serializers.order import OrderListSerializer, OrderSerializer
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
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ("train_type",)
    search_fields = ("name",)

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
            serializer = RouteListSerializer

        if self.action == "retrieve":
            serializer = RouteDetailSerializer

        return serializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    filter_backends = (SearchFilter,)
    search_fields = ("name",)


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("route__source_id", "route__destination_id")

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
            queryset = (
                queryset.select_related(
                    "train__train_type",
                    "route__destination",
                    "route__source",
                )
                .prefetch_related("crews")
                .annotate(
                    sold_tickets=Count("tickets"),
                    tickets_available=(
                        F("train__places_per_car") * F("train__car_count")
                        - Count("tickets")
                    ),
                )
            )

        return queryset


class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ("first_name", "last_name")

    def get_serializer_class(self):
        serializer = CrewSerializer

        if self.action == "list":
            serializer = CrewShortSerializer

        if self.action == "retrieve":
            serializer = CrewDetailSerializer

        return serializer

    def get_queryset(self):
        queryset = self.queryset

        if self.action == "retrieve":
            queryset = queryset.prefetch_related(
                Prefetch(
                    "trips",
                    queryset=Trip.objects.select_related(
                        "train",
                        "route__source",
                        "route__destination",
                    ),
                )
            )

        return queryset


class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Order.objects.all()

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)

        if self.action in ("list", "retrieve"):
            queryset = queryset.prefetch_related("tickets")

        return queryset

    def get_serializer_class(self):
        serializer = OrderSerializer

        if self.action == "list":
            serializer = OrderListSerializer

        return serializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
