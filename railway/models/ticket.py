from django.db import models
from django.db.models import UniqueConstraint
from rest_framework.exceptions import ValidationError


class Ticket(models.Model):
    car = models.PositiveIntegerField()
    seat = models.PositiveIntegerField()
    trip = models.ForeignKey(
        "Trip",
        on_delete=models.CASCADE,
        related_name="tickets",
    )
    order = models.ForeignKey(
        "Order",
        on_delete=models.CASCADE,
        related_name="tickets",
    )

    class Meta:
        ordering = ("seat",)
        constraints = [
            UniqueConstraint(
                fields=("car", "seat", "trip"),
                name="unique_trip_car_seat",
            )
        ]

    def __str__(self):
        return f"{self.trip} - (seat: {self.seat})"

    @staticmethod
    def validate_seat(
            seat: int,
            num_seats: int,
            car_count: int,
            car: int,
            error_to_raise,
    ):
        if seat < 1 or seat > num_seats:
            raise error_to_raise({
                "seat": f"seat must be between 1 and {num_seats}"
            })

        if car < 1 or car > car_count:
            raise error_to_raise({
                "car": f"car must be between 1 and {car_count}"
            })

    def clen(self):
        self.validate_seat(
            seat=self.seat,
            num_seats=self.trip.train.places_per_car,
            car_count=self.trip.train.car_count,
            car=self.car,
            error_to_raise=ValidationError,
        )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Ticket, self).save(*args, **kwargs)
