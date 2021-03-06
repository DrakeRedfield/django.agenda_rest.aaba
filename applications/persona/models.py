#
from model_utils.models import TimeStampedModel
#
from django.db import models

from .managers import *

class Hobby(TimeStampedModel):
    name = models.CharField(
        'Pasatiempo',
        max_length = 50
    )

    class Meta:
        verbose_name = 'Hobby'
        verbose_name_plural = 'Hobbies'

    def __str__(self):
        return self.name

class Person(TimeStampedModel):
    """  Modelo para registrar personas de una agenda  """

    full_name = models.CharField(
        'Nombres', 
        max_length=50,
    )
    job = models.CharField(
        'Trabajo', 
        max_length=30,
        blank=True
    )
    email = models.EmailField(
        blank=True, 
        null=True
    )
    phone = models.CharField(
        'telefono',
        max_length=15,
        blank=True,
    )

    hobbies = models.ManyToManyField(Hobby)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    def __str__(self):
        return self.full_name

class Meet(TimeStampedModel):
    persona = models.ForeignKey(
        Person,
        on_delete = models.CASCADE
    )
    fecha = models.DateField()
    hora = models.TimeField()
    asunto = models.CharField(
        'Asunto',
        max_length = 100
    )

    objects = ReunionMagager()
    
    class Meta:
        verbose_name = 'Meeting'
        verbose_name_plural = 'Meeting'

    def __str__(self):
        return self.asunto