# third-party
from model_utils.models import TimeStampedModel
from django_countries.fields import CountryField

# django
from django.db import models

# local

from applications.tours.models import Tour


class Order(TimeStampedModel):
    """Model definition for Order."""

    PAYMENT_CREDIT_CARD = 'C'
    PAYMENT_PAYPAL = 'P'
    PAYMENT_CHOICES = (
        (PAYMENT_CREDIT_CARD, 'tarjeta de credito'),
        (PAYMENT_PAYPAL, 'Paypal'),
    )

    full_name = models.CharField('nombre completo', max_length=100)
    email = models.EmailField(max_length=100)
    postal_code = models.CharField('codigo postal', max_length=10)
    country = CountryField(verbose_name="país")
    payment_type = models.CharField('tipo de pago', max_length=1, choices=PAYMENT_CHOICES, default="P")
    payment_id = models.CharField('id de pago', max_length=15)


    class Meta:
        """Meta definition for Order."""

        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        """Unicode representation of Order."""
        return self.full_name


class OrderItem(TimeStampedModel):
    """Model definition for OrderItem."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    quantity  = models.PositiveIntegerField('cantidad')
    price = models.DecimalField('precio', max_digits=10, decimal_places=2)

    class Meta:
        """Meta definition for OrderItem."""

        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'

    def __str__(self):
        """Unicode representation of OrderItem."""
        return '%s - %s' %(str(self.order), self.tour)
