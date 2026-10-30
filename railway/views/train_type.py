from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from railway.models.train_type import TrainType
from railway.permissions import IsAdminOrIfAuthenticatedReadOnly
from railway.serializers.train_type import TrainTypeSerializer


class TrainTypeViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    queryset = TrainType.objects.all()
    serializer_class = TrainTypeSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
