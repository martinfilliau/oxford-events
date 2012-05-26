from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api

from oxford_events.events.api import EventResource

admin.autodiscover()

api = Api(api_name='v1')
api.register(EventResource())

urlpatterns = patterns('',
    url(r'^search/', include('haystack.urls')),
    url(r'^api/', include(api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
