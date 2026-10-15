from django.db import models


class Trip(models.Model):
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    route = models.ForeignKey(
        "Route",
        on_delete=models.CASCADE,
        related_name="trips",
    )
    train = models.ForeignKey(
        "Train",
        on_delete=models.CASCADE,
        related_name="trips",
    )

    def __str__(self):
        return f"id: ({self.id}) {self.departure_time} - {self.arrival_time}"
