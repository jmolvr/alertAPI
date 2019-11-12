from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class AlertView(APIView):
    def get(self, request):
        alertas = Alert.objects.all()
        serializer = AlertSerializer(alertas, many=True)
        return Response(serializer.data)

    def post(self, request):
        alerta = request.data.get('alerta')
        serializer = AlertSerializer(data=alerta)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response(serializer.data)


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer


class LocalUnifapViewSet(viewsets.ModelViewSet):
    queryset = LocalUnifap.objects.all()
    serializer_class = LocalUnifapSerializer
