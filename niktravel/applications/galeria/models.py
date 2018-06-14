# third-party
from model_utils.models import TimeStampedModel

# django
from django.db import models

# local
from applications.tours.models import Tour

# Create your models here.


class Photo(TimeStampedModel):
    """Model definition for Photo."""

    # TODO: Define fields here
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    description = models.CharField('descripcion', max_length=50)
    image = models.ImageField('imagen', upload_to='gallery')


    class Meta:
        """Meta definition for Photo."""

        verbose_name = 'foto'

    def __str__(self):
        """Unicode representation of Photo."""
        return self.description
