from rest_framework import viewsets

from station.models.train import Train
from station.serializers.train import TrainSerializer


class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
