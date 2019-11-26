from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from .permissions import isOwner
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.order_by('-created_at')
    serializer_class = AlertSerializer
    permission_classes = [isOwner, IsAuthenticatedOrReadOnly]


class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoCustomSerializer


class LocalUnifapViewSet(viewsets.ModelViewSet):
    queryset = LocalUnifap.objects.all()
    serializer_class = LocalUnifapSerializer
