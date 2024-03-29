from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

import flashpolicies

urlpatterns = patterns('',
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^watch_latest/','watch.views.watch_latest'),
                       url(r'^episode/([a-zA-Z0-9\w\ ]+)/(\d+)', 'videos.views.video'),

                       url(r'^like/([a-zA-Z0-9\w\ ]+)','profile.views.like'),
                       url(r'^fav/([a-zA-Z0-9\w\ ]+)','profile.views.fav'),       

                       url(r'^get_programs/([a-zA-Z0-9\w\ ]+)', 'videos.views.channel_programs'),
                       url(r'^get_videos/([a-zA-Z0-9\w\ ]+)', 'videos.views.program_videos'),
                       url(r'^get_channels/([a-zA-Z0-9\w\ ]+)', 'videos.views.network_channels'),

                       url(r'^login/$', 'profile.views.site_login'),
                       url(r'^logout/$', 'profile.views.site_logout'),

                       url(r'^crossdomain.xml$',
                           'flashpolicies.views.simple',
                           {'domains': ['127.0.0.1:8000']}),

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
