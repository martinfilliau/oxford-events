from haystack import indexes

from oxford_events.events.models import Event

class EventIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    comments = indexes.CharField(model_attr='comments')
    start_at = indexes.DateTimeField(model_attr='start_at')

    def get_model(self):
        return Event

    def index_queryset(self):
        return self.get_model().objects.all()
