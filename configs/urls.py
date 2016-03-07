"""demo_terms URL Configuration."""
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^dicom/', include('sil_dicom.urls',
        namespace='sil_dicom'))
]

urlpatterns = format_suffix_patterns(
    urlpatterns, allowed=['json', 'html', 'xml'])
