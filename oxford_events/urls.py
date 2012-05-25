from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oxford_events.views.home', name='home'),
    # url(r'^oxford_events/', include('oxford_events.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
