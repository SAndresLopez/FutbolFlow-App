from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from app_futbol.Seguridad import limpiar_texto

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

    @property
    def estado_dinamico(self):
        ahora = timezone.now()
        inscritos_count = self.Inscripcion.count()

        if ahora > self.fecha:
            return "Finalizado o En curso"

        if inscritos_count >= self.cupos_max:
            return "Cupos Llenos"

        return "Disponible"

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
    estrellas = models.DecimalField(max_digits=3, decimal_places=2, default=5.0)
    partidos_jugados = models.IntegerField(default=0)
    foto = models.ImageField(upload_to='perfiles/', null=True, blank=True, verbose_name="Foto de Crack")
    puntos = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Perfil de Jugador"
        verbose_name_plural = "Perfiles de Jugadores"

    def __str__(self):
        return f"{self.usuario.username} - {self.apodo if self.apodo else self.posicion}"


class Inscripcion(models.Model):
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, related_name='Inscripcion')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mis_inscripciones')
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    equipo = models.CharField(max_length=1, choices=[('A', 'Equipo A'), ('B', 'Equipo B')])
    posicion_numero = models.IntegerField()

    class Meta:
        unique_together = ('partido', 'equipo', 'posicion_numero')

    def __str__(self):
        return f"{self.usuario} en {self.partido.nombre_encuentro}"


class Reporte(models.Model):
    TIPOS_REPORTE = [
        ('CONDUCTA', 'Conducta Antideportiva'),
        ('FALLO', 'Fallo del Sistema / Bug'),
        ('PAGO', 'Problema con Pago/Voucher'),
        ('OTRO', 'Otro'),
    ]

    ESTADOS_REPORTE = [
        ('PENDIENTE', 'Pendiente de Revisión'),
        ('EN_PROCESO', 'En Revisión'),
        ('RESUELTO', 'Resuelto'),
        ('RECHAZADO', 'Rechazado'),
    ]

    usuario_creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mis_reportes')
    usuario_reportado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                          related_name='reportes_recibidos')
    partido = models.ForeignKey('Partido', on_delete=models.SET_NULL, null=True, blank=True)

    tipo = models.CharField(max_length=50, choices=TIPOS_REPORTE, default='CONDUCTA')
    descripcion = models.TextField(verbose_name="Detalles del reporte")
    captura = models.ImageField(upload_to='reportes/', null=True, blank=True, verbose_name="Evidencia (Opcional)")

    estado = models.CharField(max_length=20, choices=ESTADOS_REPORTE, default='PENDIENTE')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    notas_admin = models.TextField(null=True, blank=True, verbose_name="Comentarios del Administrador")

    def __str__(self):
        return f"Reporte {self.id} - {self.tipo} por {self.usuario_creador.username}"

    def save(self, *args, **kwargs):
        self.descripcion = limpiar_texto(self.descripcion)
        super().save(*args, **kwargs)

class Ranking(models.Model):
    jugador = models.OneToOneField('PerfilJugador', on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0)
    partidos_jugados = models.IntegerField(default=0)
    nivel = models.CharField(max_length=20, default='Bronce')

    class Meta:
        ordering = ['-puntos']
