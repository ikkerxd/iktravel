# django
from django.views.generic import DetailView, FormView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse

# local
from applications.galeria.models import Photo
from applications.itinerario.models import Itinerary
from .models import Tour

from .forms import CartForm

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


class CartView(SingleObjectMixin, FormView):
    '''
    Carrito de compra del tour
    '''
    model = Tour
    template_name = "tours/cart.html"
    context_object_name = 'tour'
    form_class = CartForm

    def get(self, *args, **kwargs):
        self.object = self.get_object()
        return super().get(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # creamos una session para poder mandar el valor de la cantidad a otra vista
        request.session['quantity'] = request.POST['quantity']
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse(
            'tours_app:payment',
            kwargs={
                'category': self.object.category,
                'slug': self.object.slug,
            }
        )


class PaymentView(SingleObjectMixin, FormView):
    model = Tour
    template_name = "tours/payment.html"
    context_object_name = 'tour'
    form_class = CartForm

    def get_context_data(self, **kwargs):
        context = super(PaymentView, self).get_context_data(**kwargs)
        print('______________________session____________________________')
        quantity = self.request.session.get('quantity')
        price = self.object.price_des_dolar
        print(type(quantity))
        print(type(price))
        print(price)
        print(quantity)
        total = int(quantity) * price
        print(total)
        context['quantity'] = quantity
        context['total'] = total
        return context

    def get(self, *args, **kwargs):
        self.object = self.get_object()
        return super().get(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('/', kwargs={'pk': self.pk})