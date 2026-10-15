from django.urls import include, path
from rest_framework import routers

from station.views import TrainTypeViewSet, TrainViewSet

router = routers.DefaultRouter()

router.register("trains", TrainViewSet,)
router.register("train-types", TrainTypeViewSet,)

urlpatterns = (
    path("", include(router.urls)),
)

app_name = "station"
