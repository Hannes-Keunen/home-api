from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('device', views.DeviceViewSet)
router.register('template', views.TemplateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('device/<int:pk>/state', views.device_state),
]