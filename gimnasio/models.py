from django.db import models
from django.urls import reverse

# 1. Modelo Padre (Clasificador) - Administrado exclusivamente en el Django Admin
class TipoEquipamiento(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Tipo de Equipamiento")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    def __str__(self):
        return self.nombre

# 2. Modelo Hijo (Operativo / Transaccional con 4 campos propios y ForeignKey)
class ImplementoGym(models.Model):
    # Relación 1:N obligatoria
    tipo = models.ForeignKey(TipoEquipamiento, on_delete=models.CASCADE, verbose_name="Tipo de Equipamiento")
    
    # 4 Campos propios requeridos por la pauta (Texto, Decimal, Fecha, Booleano)
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Implemento")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio ($)")
    fecha_adquisicion = models.DateField(verbose_name="Fecha de Adquisición")
    disponible = models.BooleanField(default=True, verbose_name="¿Disponible en stock?")

    def get_absolute_url(self):
        return reverse('catalogo_implementos')

    def __str__(self):
        return f"{self.nombre} ({self.tipo.nombre})"