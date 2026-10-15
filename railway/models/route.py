from django.db import models
from django.db.models import UniqueConstraint


class Route(models.Model):
    source = models.ForeignKey(
        "Station",
        on_delete=models.CASCADE,
        related_name="routes",
    )
    destination = models.ForeignKey(
        "Station",
        on_delete=models.CASCADE,
        related_name="routes",
    )
    distance = models.PositiveIntegerField()

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["source", "destination"],
                name="unique_route"
            )
        ]

    def str(self):
        return (
            f"{self.source.name} - {self.destination.name} "
            f"(distance: {self.distance})"
        )
