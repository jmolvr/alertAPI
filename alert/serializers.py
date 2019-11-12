from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist,  ValidationError
from .models import *


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        exclude = []


class LocalUnifapSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalUnifap
        exclude = []


class AlertSerializer(serializers.ModelSerializer):
    #tipo = CustomTipoField(fields=('id', 'nome'), read_only=True)
    #tipo = TipoSerializer(read_only=True)

    class Meta:
        model = Alert
        exclude = []

    def create(self, validated_data):
        print(validated_data)
        return Alert.objects.create(**validated_data)
