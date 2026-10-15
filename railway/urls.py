from django.urls import include, path
from rest_framework import routers

from railway.views import (
    RouteViewSet,
    StationViewSet,
    TrainTypeViewSet,
    TrainViewSet,
    TripViewSet,
)

router = routers.DefaultRouter()

router.register("trains", TrainViewSet,)
router.register("train-types", TrainTypeViewSet,)
router.register("routes", RouteViewSet,)
router.register("stations", StationViewSet,)
router.register("trips", TripViewSet,)

urlpatterns = (
    path("", include(router.urls)),
)

app_name = "railway"
