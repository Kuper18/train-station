from django.db.models import Prefetch
from rest_framework import mixins
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet

from railway.models import Crew
from railway.models.trip import Trip
from railway.permissions import IsAdminOrIfAuthenticatedReadOnly
from railway.serializers.crew import CrewDetailSerializer, CrewSerializer
from railway.serializers.crew_short_serializer import CrewShortSerializer


class CrewViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Crew.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ("first_name", "last_name")
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

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
