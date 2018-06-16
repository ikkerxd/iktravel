# django
from django.views.generic import TemplateView

# local
from applications.tours.models import Tour


class IndexView(TemplateView):
    """
    Vista de inicio(index) de inkatravel vip
    """
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['ofertas'] = Tour.objects.all()
        context['tours'] = Tour.objects.all()
        return context
    