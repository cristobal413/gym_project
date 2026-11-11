from django.contrib import admin
from .models import TipoEquipamiento, ImplementoGym

@admin.register(TipoEquipamiento)
class TipoEquipamientoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(ImplementoGym)
class ImplementoGymAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo', 'precio', 'fecha_adquisicion', 'disponible')
    list_filter = ('tipo', 'disponible')
    search_fields = ('nombre',)