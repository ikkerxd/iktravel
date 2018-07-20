from django.urls import path
from . import views
from .paypal import paypal_create, paypal_execute

app_name = "order_app"

urlpatterns = [
    # urls para la aplicacion order
    # path(
    #     r'paypal/create/',
    #     paypal_create,
    #     name='paypal_create'
    # ),
    path(
        r'paypal/execute/',
        paypal_execute,
        name='paypal_execute'
    ),
]
