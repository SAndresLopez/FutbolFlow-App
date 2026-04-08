from django.db import models


class Partido(models.Model):
    nombre_encuentro = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cupos_disponibles = models.IntegerField(default=12)
    cupos_max = models.IntegerField(default=12)

    def __str__(self):
        return f"{self.lugar} - {self.fecha.strftime('%d/%m/%Y')}"

    @property
    def cupos_ocupados(self):
        return self.cupos_max - self.cupos_disponibles

    @property
    def porcentaje_llenado(self):
        if self.cupos_max > 0:
            porcentaje = (self.cupos_ocupados / self.cupos_max) * 100
            return min(porcentaje, 100)
        return 0


from django.contrib.auth.models import User

class PerfilJugador(models.Model):
    # Esto vincula el perfil con el usuario de Django
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    # Tus campos personalizados
    posicion = models.CharField(max_length=50, choices=[
        ('Portero', 'Portero'),
        ('Defensa', 'Defensa'),
        ('Mediocampista', 'Mediocampista'),
        ('Delantero', 'Delantero'),
    ], default='Mediocampista')

    class Meta:
        verbose_name = "Perfil de Jugador"
        verbose_name_plural = "Perfiles de Jugadores"

    ranking = models.DecimalField(max_digits=3, decimal_places=2, default=5.0)

    def __str__(self):
        return f"{self.usuario.username} - {self.posicion}"