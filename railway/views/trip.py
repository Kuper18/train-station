from django.db.models import Count, F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from railway.models.trip import Trip
from railway.permissions import IsAdminOrIfAuthenticatedReadOnly
from railway.serializers.trip import (
    TripDetailSerializer,
    TripListSerializer,
    TripSerializer,
)


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("route__source_id", "route__destination_id")
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

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
