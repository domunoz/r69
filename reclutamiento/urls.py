from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'siniestros.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(admin.site.urls)),
#   url(r'^postulantes/', include('postulantes.urls')),
)

admin.site.site_header = 'Reclutamiento'
