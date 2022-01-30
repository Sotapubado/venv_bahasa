from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path, include
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include('bahasa1.urls')),
    path('accounts/', include('allauth.urls')),
    

    path('after/', include('after.urls')),
    path('salon/', include('salon.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
