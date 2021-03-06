from django.urls import re_path
from alert import consumers

websocket_urlpatterns = [
    re_path(r'ws/alertas/(?P<room_name>\w+)/$', consumers.AlertConsumer)
]
