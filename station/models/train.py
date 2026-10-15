from django.db import models

from station.models.train_type import TrainType


class Train(models.Model):
    name = models.CharField(max_length=200)
    car_count = models.PositiveIntegerField()
    places_per_car = models.PositiveIntegerField()
    train_type = models.ForeignKey(
        TrainType,
        on_delete=models.PROTECT,
        related_name="trains",
    )
