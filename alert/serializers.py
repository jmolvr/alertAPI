from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist,  ValidationError
from .models import Alert, Tipo, LocalUnifap
from user.serializers import UserSerializer
from channels.layers import get_channel_layer


class TipoCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        exclude = []


class LocalUnifapSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalUnifap
        exclude = []


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        exclude = []

    def create(self, validated_data):
        return Alert.objects.create(**validated_data)

    def update(self, instance, validate_data):
        request = self.context['request']
        if request.user.is_admin:
            instance.descricao = instance.descricao
            instance.prazo = validate_data.get('prazo', instance.prazo)
        else:
            instance.descricao = validate_data.get(
                'descricao', instance.descricao)
        instance.status = validate_data.get('status', instance.status)

        instance.save()
        return instance

    def to_internal_value(self, data):
        request = self.context['request']

        if request.method == "PUT":
            return self.put_validate_data(request, data)

        latitude = data.get('latitude')
        longitude = data.get('longitude')
        descricao = data.get('descricao')
        local = data.get('local')
        tipo = data.get('tipo')

        if latitude is None:
            raise serializers.ValidationError({
                'latitude': 'This field is required'
            })

        if longitude is None:
            raise serializers.ValidationError({
                'longitude': 'This field is required'
            })

        if not descricao:
            raise serializers.ValidationError({
                'descricao': 'This field is required'
            })

        if not local:
            raise serializers.ValidationError({
                'local': 'This field is required'
            })

        if not tipo:
            raise serializers.ValidationError({
                'tipo': 'This field is required'
            })

        try:
            tipo = Tipo.objects.get(nome=tipo)
        except:
            raise serializers.ValidationError({
                'tipo': 'Tipo {} não está registrado'.format(tipo)
            })

        try:
            local = LocalUnifap.objects.get(nome=local)
        except:
            raise serializers.ValidationError({
                'local': 'Local {} não está registrado'.format(local)
            })

        return {
            'latitude': latitude,
            'longitude': longitude,
            'descricao': descricao,
            'tipo': tipo,
            'local': local,
            'owner': request.user,
        }

    def to_representation(self, obj):
        return{
            'id': obj.id,
            'latitude': obj.latitude,
            'longitude': obj.longitude,
            'descricao': obj.descricao,
            'tipo': TipoCustomSerializer(obj.tipo).data,
            'prazo': obj.prazo,
            'local': LocalUnifapSerializer(obj.local).data,
            'status': obj.status,
            'created_at': str(obj.created_at),
            'owner': UserSerializer(obj.owner).data
        }

    def put_validate_data(self, request, data):
        descricao = data.get("descricao")
        prazo = data.get('prazo')
        status = data.get('status')

        return({
            'descricao': descricao,
            'prazo': prazo,
            'status': status,
        })

    @staticmethod
    def get_group():
        return 'alertas'
