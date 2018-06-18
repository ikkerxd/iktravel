# third-party
from model_utils.models import TimeStampedModel

# django
from django.db import models

# local
from applications.tours.models import Tour

# Create your models here.


class Itinerary(TimeStampedModel):
    """Model definition for Itinerary."""

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    day = models.CharField('dia(s)', max_length=5)
    title = models.CharField('titulo', max_length=50)
    description_es = models.TextField(verbose_name='descripcion en español')
    description_en = models.TextField(verbose_name='descripcion en ingles', blank=True, null=True)
    description_pt = models.TextField(verbose_name='descripcion en español', blank=True, null=True)

    class Meta:
        """Meta definition for Itinerary."""

        verbose_name = 'Itinerario'
        ordering = ['created']

    def __str__(self):
        """Unicode representation of Itinerary."""
        return self.description_es
