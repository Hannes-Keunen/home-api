from rest_framework import serializers

from . import models

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Device
        fields = ['url', 'address']