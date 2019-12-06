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
    tipo = TipoCustomSerializer(read_only=True)
    local = LocalUnifapSerializer(read_only=True)
    owner = UserSerializer(read_only=True)

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
            instance.feedback = validate_data.get(
                'feedback', instance.feedback)
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
        image = data.get('image')

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
            local = LocalUnifap(nome=local)
            local.save()

        return {
            'latitude': latitude,
            'longitude': longitude,
            'descricao': descricao,
            'tipo': tipo,
            'local': local,
            'image': image,
            'owner': request.user,
        }

    def put_validate_data(self, request, data):
        descricao = data.get("descricao")
        prazo = data.get('prazo')
        status = data.get('status')
        feedback = data.get('feedback')

        return({
            'descricao': descricao,
            'prazo': prazo,
            'status': status,
            'feedback': feedback
        })

    @staticmethod
    def get_group():
        return 'alertas'
