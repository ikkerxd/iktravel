from django.urls import path
from . import views

app_name = "tours_app"

urlpatterns = [
    # urls para la aplicacion tours
    path(
        r'<str:category>/<slug:slug>',
        views.TourDetailView.as_view(),
        name='detail'
    ),
    path(
        r'<str:category>/<slug:slug>/cart/',
        views.CartView.as_view(),
        name='cart'
    ),
    path(
        r'<str:category>/<slug:slug>/payment/',
        views.PaymentView.as_view(),
        name='payment'
    ),
]
