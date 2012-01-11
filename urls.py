from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^watch_latest/','watch.views.watch_latest'),
                       url(r'^episode/([a-zA-Z0-9\w\ ]+)/(\d+)', 'videos.views.video'),

                       url(r'^like/([a-zA-Z0-9\w\ ]+)','profile.views.like'),
                       url(r'^fav/([a-zA-Z0-9\w\ ]+)','profile.views.fav'),       

                       url(r'^$','frontpage.views.frontpage'),
)



# SERVING MEDIA_ROOT
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True,
        }),
   )

#Static files
urlpatterns += staticfiles_urlpatterns()   
