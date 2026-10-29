from django.db import models

from railway.models.train_type import TrainType


class Train(models.Model):
    name = models.CharField(max_length=200)
    car_count = models.PositiveIntegerField()
    places_per_car = models.PositiveIntegerField()
    train_type = models.ForeignKey(
        TrainType,
        on_delete=models.PROTECT,
        related_name="trains",
    )

    @property
    def total_seats(self):
        return self.car_count * self.places_per_car

    def __str__(self):
        return f"{self.name} type: {self.train_type.name}"
