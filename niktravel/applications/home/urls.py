from django.urls import include, path
from . import views

app_name="home_app"

urlpatterns = [
    # urls para la aplicacion home
    path(
        r'',
        views.IndexView.as_view(),
        name='index'
    ),
]
