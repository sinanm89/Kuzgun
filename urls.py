from django.conf.urls.defaults import patterns, include, url

from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kuzgun.views.home', name='home'),
    # url(r'^kuzgun/', include('kuzgun.foo.urls')),
                          url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                          url(r'^admin/', include(admin.site.urls)),
                          url(r'^watch/','watch.views.watch'),
)


# SERVING MEDIA_ROOT
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )