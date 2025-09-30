from django.db import models

class Cliente(models.Model):
    nombres   = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    dni       = models.CharField(max_length=20, unique=True) 
    email     = models.EmailField(blank=True, null=True)
    telefono  = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    ciudad    = models.CharField(max_length=80, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    creado_en  = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["apellidos", "nombres"]

    def __str__(self):
        return f"{self.apellidos}, {self.nombres} ({self.dni})"
