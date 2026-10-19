from django.urls import include, path
from rest_framework import routers

from railway.views import (
    CrewViewSet,
    OrderViewSet,
    RouteViewSet,
    StationViewSet,
    TrainTypeViewSet,
    TrainViewSet,
    TripViewSet,
)

router = routers.DefaultRouter()

router.register("trains", TrainViewSet)
router.register("train-types", TrainTypeViewSet)
router.register("routes", RouteViewSet)
router.register("stations", StationViewSet)
router.register("trips", TripViewSet)
router.register("crews", CrewViewSet)
router.register("orders", OrderViewSet)

urlpatterns = (
    path("", include(router.urls)),
)

app_name = "railway"
