from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Docente(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)
    celular = models.CharField(max_length=9)
    email = models.EmailField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.apellidos} {self.nombres}'

    class Meta:
        db_table = 'teachers'
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ['id']


class Modalidad(models.Model):
    id = models.AutoField(primary_key=True)
    modalidad = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.modalidad}'

    class Meta:
        db_table = 'modalities'
        verbose_name = 'Modality'      
        verbose_name_plural = 'Modalities'
        ordering = ['id']


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.categoria}'

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

        
class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    curso = models.CharField(max_length=255)
    duracion = models.IntegerField()
    precio = models.DecimalField(decimal_places=2)
    id_categoria = ForeignKey(Categoria)
    id_modalidad = ForeignKey(Modalidad)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.curso}'

    class Meta:
        db_table = 'courses'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']
    

class PeriodoLectivo(models.Model):
    id = models.AutoField(primary_key=True)
    perido = models.CharField(max_length=255)
    id_curso = models.ForeignKey(Curso)
    fechaInicio = models.DateTimeField()
    fehaCierre = models.DateTimeField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.perido}'

    class Meta:
        db_table = 'periodo_lectivo'
        verbose_name = 'Periodo Lectivo'
        verbose_name_plural = 'Periodos Lectivos'
        ordering = ['id']


class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    frecuencia = models.CharField(max_length=50)
    horaInicio = models.CharField(max_length=12)
    horaFin = models.CharField(max_length=12)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.frecuencia} {self.horaInicio} - {self.horaFin}'

    class Meta:
        db_table = 'horarios'
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering = ['frecuencia']


class HorarioCurso(models.Model):
    id = models.AutoField(primary_key=True)
    id_horario = models.ForeignKey(Horario)
    id_curso = models.ForeignKey(Curso)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id_horario}-{self.id_curso}'

    class Meta:
        db_table = 'horario_curso'
        verbose_name = 'Horario de Curso'
        verbose_name_plural = 'Horario de Cursos'
        ordering = ['id']