# standard library
from datetime import timedelta, datetime

# third-party
from model_utils.models import TimeStampedModel

# django
from django.db import models
from django.template.defaultfilters import slugify

# local
from applications.miscelanea.models import Category, Include, NoInclude


class Tour(TimeStampedModel):
    """Model definition for Tour."""

    name = models.CharField('nombre', max_length=80) # Nombre del tour
    place  = models.CharField('lugar', max_length=50) # Lugar del tour
    duration = models.IntegerField('duracion') # duracion en dias U horas del tour
    cover = models.ImageField('portada', upload_to='portada') # portada del tour
    video = models.CharField('video', max_length=250) # frame de la url del tour
    description_es = models.TextField('descripcion en español') # descripcion en ingles del tour
    description_en = models.TextField('descripcion en ingles', blank=True, null=True) # descripcion en portugues del tour
    description_pt = models.TextField('descripcion en portugues', blank=True, null=True) # descripcion en portugues del tour
    price_sol = models.DecimalField(
        'precio en soles',
        max_digits=6,
        decimal_places=2,
        default=0
    ) # Precio en soles del tour
    price_des_sol = models.DecimalField(
        'precio en con descuento soles',
        blank=True,
        null=True,
        max_digits=6,
        decimal_places=2,
        default=0
    ) # Precio con descuento en soles del tour
    price_dolar = models.DecimalField(
        'precio en dolares',
        max_digits=6,
        decimal_places=2,
        default=0
    ) # Precio en dolares del tour
    price_des_dolar = models.DecimalField(
        'precio con descuento en dolares',
        blank=True,
        null=True,
        max_digits=6,
        decimal_places=2,
        default=0
    ) # Precio con descuento en dolares del tour
    category = models.ForeignKey(
        Category,
        verbose_name='categoria',
        on_delete=models.CASCADE
    ) # Categoria del tour
    include = models.ManyToManyField(
        Include,
        verbose_name='Que incluye',
    ) # Servicios q inclyue le tour
    no_include = models.ManyToManyField(
        NoInclude,
        verbose_name='que no incluye',
    ) # Servisios q no incluye el tour
    slug = models.SlugField(editable=False, max_length=200)
    
    class Meta:
        """Meta definition for Tour."""

        verbose_name = 'Tour'
        ordering = ['-created']

    def __str__(self):
        """Unicode representation of Tour."""
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # calculamos el total de segundos de la hora actual
            now = datetime.now()
            total_time = timedelta(
                hours=now.hour,
                minutes=now.minute,
                seconds=now.second
            )
            seconds = int(total_time.total_seconds())
            slug_unique = '%s %s' % (self.name, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.name, str(seconds))

        self.slug = slugify(slug_unique)
        super(Tour, self).save(*args, **kwargs)
