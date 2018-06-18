from django.urls import include, path
from . import views


app_name="tours_app"

urlpatterns = [
    # urls para la aplicacion tours
    path(
        r'<str:category>/<slug:slug>',
        views.TourDetailView.as_view(),
        name='detail'
    ),
]
