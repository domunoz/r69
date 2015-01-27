from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'siniestros.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cargos/', 'postulantes.views.upload'),
    url(r'^medios/', 'postulantes.views.upload'),
    url(r'^comunas/', 'postulantes.views.upload'),

    
)
