from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from alert.models import Alert
from alert.serializers import AlertSerializer
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class AlertConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        group_name = AlertSerializer.get_group()

        await self.channel_layer.group_add(
            group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            AlertSerializer.get_group(),
            self.channel_name
        )

    async def receive_json(self, text_data):
        group_name = "alertas"
        self.groups.append(group_name)

    async def notify(self, event):
        await self.send_json(event['content'])


@receiver([post_save, post_delete], sender=Alert)
def update_alerts(sender, instance, **kwargs):
    alertas = Alert.objects.order_by('-created_at')
    serializer = AlertSerializer(alertas, many=True)
    group_name = AlertSerializer.get_group()
    channel_layer = get_channel_layer()
    content = {
        "type": "UPDATE_ALERTS",
        "payload": serializer.data
    }

    async_to_sync(channel_layer.group_send)(
        group_name, {
            "type": "notify",
            "content": content,
        }
    )
