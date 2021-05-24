from django.contrib import admin
from .models import Transportadoras
# Register your models here.

@admin.register(Transportadoras)
class TransportadorasAdmin(admin.ModelAdmin):
    pass
