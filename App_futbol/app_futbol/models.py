from django.db import models
from django.contrib.auth.models import User

class Partido(models.Model):
    nombre_encuentro = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cupos_inscritos = models.IntegerField(default=0)
    cupos_max = models.IntegerField(default=12)


    def __str__(self):
        return f"{self.lugar} - {self.fecha.strftime('%d/%m/%Y')}"

    @property
    def cupos_restantes(self):
        return self.cupos_max - self.cupos_cupos_inscritos

    @property
    def porcentaje_llenado(self):
        if self.cupos_max > 0:
            porcentaje = (self.cupos_inscritos / self.cupos_max) * 100
            return min(porcentaje, 100)
        return 0


from django.contrib.auth.models import User

class PerfilJugador(models.Model):
    POSICIONES = [
        ('Portero', 'Portero'),
        ('Defensa', 'Defensa'),
        ('Mediocampista', 'Mediocampista'),
        ('Delantero', 'Delantero'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')

    apodo = models.CharField(max_length=30, blank=True, verbose_name="Apodo de Crack")
    telefono = models.CharField(max_length=15, blank=True)
    distrito = models.CharField(max_length=50, blank=True)
    posicion = models.CharField(max_length=50, choices=POSICIONES, default='Mediocampista')
    ranking = models.DecimalField(max_digits=3, decimal_places=2, default=5.0)

    class Meta:
        verbose_name = "Perfil de Jugador"
        verbose_name_plural = "Perfiles de Jugadores"

    def __str__(self):
        return f"{self.usuario.username} - {self.apodo if self.apodo else self.posicion}"


class Inscripcion(models.Model):
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, related_name='inscripciones')
    usuario = models.CharField(max_length=100)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_jugador} en {self.partido.nombre_encuentro}"