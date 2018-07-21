# django
from django.views.generic import DetailView, FormView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from django.shortcuts import redirect
from django.template.defaultfilters import slugify

# local
from applications.galeria.models import Photo
from applications.itinerario.models import Itinerary
from .models import Tour

from .forms import CartForm
from applications.order.forms import OrderForm
from applications.order.paypal import paypal_create 

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
                'slug': self.object.slug,
            }
        )


class PaymentView(SingleObjectMixin, FormView):
    model = Tour
    template_name = "tours/payment.html"
    context_object_name = 'tour'
    form_class = OrderForm

    price = 0.00
    quantity = 0
    total = 0.00

    def get_context_data(self, **kwargs):
        context = super(PaymentView, self).get_context_data(**kwargs)
        print('______________________session____________________________')
        context['quantity'] = self.quantity
        context['total'] = self.total
        return context

    def get(self, *args, **kwargs):
        print('enteeeeeeeeeeeeeee al get')
        self.object = self.get_object()
        self.quantity = self.request.session.get('quantity')
        self.price = self.object.price_des_dolar
        self.total = int(self.quantity) * self.price

        return super().get(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('e------------entre la post')
        self.object = self.get_object()

        name = self.object.name
        price = self.object.price_des_dolar
        quantity = request.session.get('quantity')
        total = int(quantity) * price
        # redirect_url = paypal_create(request, 'henrry joel')
        return redirect(
            paypal_create(request, name, price, quantity, total)
        )
