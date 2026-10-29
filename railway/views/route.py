from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from railway.models.route import Route
from railway.permissions import IsAdminOrIfAuthenticatedReadOnly
from railway.serializers.route import (
    RouteDetailSerializer,
    RouteListSerializer,
    RouteSerializer,
)


class RouteViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Route.objects.select_related("source", "destination")
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_serializer_class(self):
        serializer = RouteSerializer

        if self.action == "list":
            serializer = RouteListSerializer

        if self.action == "retrieve":
            serializer = RouteDetailSerializer

        return serializer
