from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from .permissions import isOwner


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [isOwner]


class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoCustomSerializer


class LocalUnifapViewSet(viewsets.ModelViewSet):
    queryset = LocalUnifap.objects.all()
    serializer_class = LocalUnifapSerializer
