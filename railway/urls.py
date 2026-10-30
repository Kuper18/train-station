from django.urls import include, path
from rest_framework import routers

from railway.views.crew import CrewViewSet
from railway.views.order import OrderViewSet
from railway.views.route import RouteViewSet
from railway.views.station import StationViewSet
from railway.views.train import TrainViewSet
from railway.views.train_type import TrainTypeViewSet
from railway.views.trip import TripViewSet

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
