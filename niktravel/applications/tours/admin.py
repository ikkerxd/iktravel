# django
from django.contrib import admin

# local
from applications.galeria.models import Photo
from applications.itinerario.models import Itinerary
from .models import Tour

class ItineraryInline(admin.StackedInline):
    '''Tabular Inline View for Itinerary'''

    model = Itinerary
    min_num = 0
    # max_num = 20
    extra = 0


class PhotoInline(admin.TabularInline):
    '''Tabular Inline View for Photo'''

    model = Photo
    max_num = 5
    extra = 5

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):

    filter_horizontal = ('include','no_include')
    inlines = [PhotoInline, ItineraryInline]
    fieldsets = (
        ('Información del tour', {
            'fields': (
                'name', 'place', 'duration', 'description_es', 'description_en', 'description_pt',
            ),
        }),
        ('Multimedia del tour', {
            'fields': (
                'cover', 'video',
            ),
        }),
        ('Costo del tour', {
            'fields': (
                ('price_sol', 'price_dolar'), ('price_des_sol', 'price_des_dolar')
            ),
        }),
        ('Opciones del tour', {
            'fields': (
                'category', 'include','no_include',
            ),
        }),
    )
