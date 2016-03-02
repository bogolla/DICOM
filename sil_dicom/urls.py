from django.conf.urls import patterns, url, include
from .views import (
    DocumentView
)

# template_name = {'template_name': 'rest_framework_docs/docs.html'}
urlpatterns = patterns(
    '',
    url(r'^capabilities/', include('rest_framework_docs.urls')),
    url(r'^studies/$',
        DocumentView.as_view(), name='studies'),
    url(r'^studies/(?P<pk>[^/]+)/$',
        DocumentView.as_view(), name='studies_details')
)
