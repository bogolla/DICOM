from django.conf.urls import patterns, url
from rest_framework import routers
from .views import (
    DocumentView,
    StudiesListView,
    StudySeriesListView,
    StudyInstancesListView,
    SeriesListView,
    InstancesListView,
    StudySeriesInstancesListView,

    RetrieveStudyView,
    RetrieveStudySeriesView,
    RetrieveStudySeriesInstanceView,

    HookViewSet,
)

# template_name = {'template_name': 'rest_framework_docs/docs.html'}
urlpatterns = patterns(
    # DICOM Web Querying Service endpoints
    url(r'^studies/$', StudiesListView.as_view(), name='studies'),
    url(r'^studies/(?P<study_id>[a-zA-Z0-9-]+)/series/$',
        StudySeriesListView.as_view(), name='study_series'),

    url(r'^studies/(?P<study_id>[a-zA-Z0-9-]+)/instances/$',
        StudyInstancesListView.as_view(), name='study_instances'),

    url(r'^series/$', SeriesListView.as_view(), name='series'),
    url(r'^instances/$', InstancesListView.as_view(), name='instances'),

    url(r'^studies/(?P<study_id>[a-zA-Z0-9-]+)' +
        '/series/(?P<series_number>[a-zA-Z0-9-]+)/instances/$',
        StudySeriesInstancesListView.as_view(), name='study_series_instances'),

    # DICOM Web Retrieve Service endpoints
    url(r'^bulk_data/$',
        DocumentView.as_view(), name='bulk_data'),

    url(r'^studies/(?P<study_id>[a-zA-Z0-9-]+)/$',
        RetrieveStudyView.as_view(), name='studies_retrieve'),

    url(r'^studies/(?P<study_id>[a-zA-Z0-9-]+)/series/(?P<series_number>[a-zA-Z0-9-]+)/$',
        RetrieveStudySeriesView.as_view(), name='study_series'),

    url(r'^studies/(?P<study_id>[a-zA-Z0-9-]+)' +
        '/series/(?P<series_number>[a-zA-Z0-9-]+)/instances/' +
        '(?P<instance_uid>[a-zA-Z0-9-]+)/$',
        RetrieveStudySeriesInstanceView.as_view(), name='study_series_instances')
)

# router = routers.DefaultRouter()
# router.register(r'webhooks', HookViewSet, 'webhook')

# urlpatterns += router.urls
