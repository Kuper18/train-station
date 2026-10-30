from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet

from railway.models.train import Train
from railway.permissions import IsAdminOrIfAuthenticatedReadOnly
from railway.serializers.train import (
    TrainDetailSerializer,
    TrainListSerializer,
    TrainSerializer,
)


class TrainViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Train.objects.select_related("train_type")
    serializer_class = TrainSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ("train_type",)
    search_fields = ("name",)
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_serializer_class(self):
        if self.action == "list":
            return TrainListSerializer

        if self.action == "retrieve":
            return TrainDetailSerializer

        return TrainSerializer
