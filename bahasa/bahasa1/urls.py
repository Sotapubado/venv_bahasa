from django.urls import path
from . import views

app_name = 'bahasa1'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about",views.AboutView.as_view(), name="about" ),
    path("info",views.InfoView.as_view(), name="info" ),
]