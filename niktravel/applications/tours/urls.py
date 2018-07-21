from django.urls import path
from . import views

app_name = "tours_app"

urlpatterns = [
    # urls para la aplicacion tours
    path(
        r'<slug:slug>',
        views.TourDetailView.as_view(),
        name='detail'
    ),
    path(
        r'<slug:slug>/cart/',
        views.CartView.as_view(),
        name='cart'
    ),
    path(
        r'<slug:slug>/payment/',
        views.PaymentView.as_view(),
        name='payment'
    ),
]
