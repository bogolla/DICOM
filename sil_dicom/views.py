from rest_framework import generics, views
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from .models import Document
from .serializers import DocumentSerializer, StudiesSerializer


class DocumentView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    parser_classes = (MultiPartParser, )

    filter_fields = (
        'patient_name', 'patient_id', 'study_instance_uid',
        'series_number', 'series_number', 'study_id'
    )
    http_method_names = ['get', 'post', 'head', 'options']


class StudiesListView(generics.ListCreateAPIView):
    """ View to list all studies in the system. """

    queryset = distinct_studies = Document.objects.order_by(
        'study_id').distinct('study_id')
    serializer_class = StudiesSerializer
    parser_classes = (MultiPartParser, )
