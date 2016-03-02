from rest_framework import generics
from rest_framework.parsers import MultiPartParser

from .models import Document
from .serializers import DocumentSerializer


class DocumentView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    parser_classes = (MultiPartParser, )

    filter_fields = (
        'patient_name', 'patient_id', 'study_instance_uid',
        'series_number', 'series_number', 'study_id'
    )
    http_method_names = ['get', 'post', 'head', 'options']
