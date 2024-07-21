from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

    class Meta:
        ordering = ["comision"]

    def __str__(self):
        return f"{self.nombre} - Comisión {self.comision}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    asistencia = models.PositiveIntegerField(default=0)
    faltas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class AsistenciaProfesor(models.Model):
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE)  # Cambia a 'Profesor'
    fecha = models.DateField()
    presente = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.profesor} - {self.fecha} - {"Presente" if self.presente else "Ausente"}'

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatars/', null=True, blank=True)

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)  # Verifica que este campo exista
    fecha_contratacion = models.DateField()  # Verifica que este campo exista

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
