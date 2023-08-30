from django.db import models


class Solicitante(models.Model):
    """Registra los datos del solicitante para control."""

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    particular = models.BooleanField(default=False)
    juzgado = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Solicitante"
        verbose_name_plural = "Solicitantes"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Solicitud(models.Model):
    """
    Modelo Solicitud

    Registra las solicitudes y datos del solicitante.
    El dato de fecha/hora límite es opcional.
    """

    solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField()
    hora_registro = models.TimeField()
    fecha_limite = models.DateTimeField(blank=True, null=True)
    hora_limite = models.TimeField(blank=True, null=True)
    descripcion = models.TextField()
    respuesta = models.FileField(upload_to="respuestas", blank=True, null=True)
    clave = models.CharField(max_length=100, blank=True, null=True)


class Registro(models.Model):
    """Modelo Registro.

    Registra las acciones realizadas sobre las solicitudes.
    """
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    evento = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    estado = models.IntegerField()

