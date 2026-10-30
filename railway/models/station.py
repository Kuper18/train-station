from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return (
            f"{self.name} (latitude: "
            f"{self.latitude} longitude: {self.longitude}"
        )
