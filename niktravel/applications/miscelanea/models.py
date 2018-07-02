# third-party
from model_utils.models import TimeStampedModel

# django
from django.db import models

# Create your models here.

class Category(TimeStampedModel):
    '''
    Modelo de django para alamcenar categorias
    '''
    name = models.CharField('nombre', max_length=50)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-created']
    
    def __str__(self):
        return self.name

class Include(TimeStampedModel):
    '''
    Modelo de django para almacenar servicios que include
    '''
    name = models.CharField('nombre', max_length=80)
    name_en = models.CharField('nombre en ingles', max_length=80, null=True, blank=True)
    name_pt = models.CharField('nombre en portugues', max_length=80, null=True, blank=True)

    class Meta:
        verbose_name = 'Incluye'
        verbose_name_plural = 'Incluye'
        ordering = ['-created']
    
    def __str__(self):
        return self.name

class NoInclude(TimeStampedModel):
    '''
    Modelo de django para almacenar servicios que no include
    '''
    name = models.CharField('nombre', max_length=80)
    name_en = models.CharField('nombre en ingles', max_length=80, null=True, blank=True)
    name_pt = models.CharField('nombre en portugues', max_length=80, null=True, blank=True)

    class Meta:
        verbose_name = 'No Incluye'
        verbose_name_plural = 'No Incluye'
        ordering = ['-created']

    def __str__(self):
        return self.name


class Recommendation(TimeStampedModel):
    '''
    Modelo de django para almacenar recomendaciones
    '''
    name = models.CharField('nombre', max_length=80)
    name_en = models.CharField('nombre en ingles', max_length=80, null=True, blank=True)
    name_pt = models.CharField('nombre en portugues', max_length=80, null=True, blank=True)

    class Meta:
        verbose_name = 'Recomendación'
        verbose_name_plural = 'Recomendaciones'
        ordering = ['-created']

    def __str__(self):
        return self.name
