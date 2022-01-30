from django.urls import path

from . import views

app_name = 'after'
urlpatterns = [
    path("after_index/", views.After_indexViews.as_view(), name="after_index"),
]