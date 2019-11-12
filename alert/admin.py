from django.contrib import admin
from .models import Alert, Tipo, LocalUnifap

admin.site.register([Alert, Tipo, LocalUnifap])
