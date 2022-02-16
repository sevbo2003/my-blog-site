from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, documet_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, documet_root=settings.STATICFILES_DIRS)