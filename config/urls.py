
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('yeni/', include('yeni.urls')),
    path('admin/', admin.site.urls),
]
