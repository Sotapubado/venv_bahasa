from django.urls import path

from . import views

app_name = 'salon'

urlpatterns = [
    path("salon_index/", views.Salon_indexView.as_view(), name="salon_index"),
    path("salon_list/", views.Salon_listView.as_view(), name="salon_list"),
    path("salon_detail/<int:pk>/", views.Salon_DetailView.as_view(), name="salon_detail"),
    path("salon_create/", views.Salon_CreateView.as_view(), name="salon_create"),
    path("salon_edit/<int:pk>/", views.Salon_EditView.as_view(), name="salon_edit"),
    path("salon_delete/<int:pk>/", views.Salon_DeleteView.as_view(), name="salon_delete"),
]
