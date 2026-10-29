from django.contrib import admin

from railway.models import Crew
from railway.models.order import Order
from railway.models.route import Route
from railway.models.station import Station
from railway.models.ticket import Ticket
from railway.models.train import Train
from railway.models.train_type import TrainType
from railway.models.trip import Trip


class TicketInline(admin.TabularInline):
    model = Ticket
    extra = 1


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    pass


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass


@admin.register(TrainType)
class TrainTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (TicketInline,)


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    pass


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    pass


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    pass


@admin.register(Crew)
class CrewAdmin(admin.ModelAdmin):
    pass
