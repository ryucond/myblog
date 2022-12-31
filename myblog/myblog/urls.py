from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
#
from django.contrib.sitemaps.views import sitemap
from applications.home.sitemap import EntrySitemap, Sitemap

urlpatterns_main = [
    path('admin/', admin.site.urls),
    path('', include('applications.users.urls', namespace='users')),
    path('', include('applications.home.urls', namespace='home')),
    path('', include('applications.entrada.urls', namespace='entrada')),
    path('', include('applications.favoritos.urls', namespace='favorite')),
    # urls para ckeditor
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls'))
]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#objeto site map que genera xml
sitemaps = {
    'site':Sitemap(
        [
            'home_app:home'
        ]
    ),
    'entradas':EntrySitemap
}

urlpatterns_sitemap = [
    path('sitemap.xml/', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns = urlpatterns_main + urlpatterns_sitemap
