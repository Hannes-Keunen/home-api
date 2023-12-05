from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

import struct

from .models import Device, StateTemplate
from .serializers import DeviceSerializer, TemplateSerializer
from . import rf24

# Create your views here.

class DeviceViewSet(viewsets.ModelViewSet):
    """
    Retrieve or edit devices
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class TemplateViewSet(viewsets.ModelViewSet):
    """
    Retrieve or edit device state templates
    """
    queryset = StateTemplate.objects.all()
    serializer_class = TemplateSerializer


@csrf_exempt
def device_state(request, pk):
    try:
        device = Device.objects.get(pk=pk)
    except:
        return HttpResponse(status=410)

    if request.method == 'GET':
        return HttpResponse(status=201)
    
    elif request.method == 'PUT':
        state = int(request.body)
        rf24.write(bytes(device.address, 'utf-8'), struct.pack('B', state))
        return HttpResponse(status=201)
