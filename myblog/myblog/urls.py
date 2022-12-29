from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.users.urls', namespace='users')),
    path('', include('applications.home.urls', namespace='home')),
    path('', include('applications.entrada.urls', namespace='entrada')),
    #path('', include('applications.favoritos.urls', namespace='favoritos')),
    # urls para ckeditor
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls'))
]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
