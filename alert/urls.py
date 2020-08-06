from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import AlertViewSet, LocalUnifapViewSet, TipoViewSet, UnsolvedAlertsViewSet

router = DefaultRouter()
router.register(r'alert', AlertViewSet, basename="alert")
router.register(r'local', LocalUnifapViewSet, basename="local")
router.register(r'tipo', TipoViewSet, basename="tipo")
router.register(r'unsolved', UnsolvedAlertsViewSet, basename="unsolved")
