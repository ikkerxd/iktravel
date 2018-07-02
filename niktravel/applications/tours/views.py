# django
from django.views.generic import DetailView

# local
from .models import Tour
from applications.galeria.models import Photo
from applications.itinerario.models import Itinerary

# Create your views here.


class TourDetailView(DetailView):
    '''
    Detalle del tour
    '''
    model = Tour
    template_name = "tours/detail.html"
    context_object_name = 'tour'

    def get_context_data(self, **kwargs):
        context = super(TourDetailView, self).get_context_data(**kwargs)
        
        itinerary = Itinerary.objects.filter(tour=self.object)
        gallery = Photo.objects.filter(tour=self.object)

        context['itinerary'] = itinerary
        context['gallery'] = gallery
        return context
