from django.urls import include, path
from rest_framework import routers

from station.views import TrainViewSet

router = routers.DefaultRouter()

router.register("trains", TrainViewSet,)

urlpatterns = (
    path("", include(router.urls)),
)

app_name = "station"
