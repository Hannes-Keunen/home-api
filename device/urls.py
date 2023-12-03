from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('', views.DeviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/state', views.device_state),
]