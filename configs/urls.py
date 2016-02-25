"""demo_terms URL Configuration."""
from django.conf.urls import include, url


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),

    url(r'^dicom/', include('sil_dicom.urls',
        namespace='sil_dicom'))
]
