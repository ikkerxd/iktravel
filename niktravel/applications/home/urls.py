from django.urls import include, re_path
from . import views

app_name="home_app"

urlpatterns = [
    # urls para la aplicacion home
    re_path(
        r'^$',
        views.IndexView.as_view(),
        name='index'
    ),
]
