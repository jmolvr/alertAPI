from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import *

router = DefaultRouter()
router.register(r'alert', AlertViewSet, base_name="alert")
router.register(r'local', LocalUnifapViewSet, base_name="local")
router.register(r'tipo', TipoViewSet, base_name="tipo")
router.register(r'unsolved', UnsolvedAlertsViewSet, base_name="unsolved")
