from tastypie.resources import ModelResource

from oxford_events.events.models import Event

class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
