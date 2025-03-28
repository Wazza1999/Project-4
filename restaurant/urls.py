from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("menu.urls"), name="menu-urls"),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    ]
