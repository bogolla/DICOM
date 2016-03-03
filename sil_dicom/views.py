from rest_framework import generics, views
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from .models import Document
from .serializers import (
    DocumentSerializer,
    StudiesSerializer,
    StudySeriesSerializer,
    StudyInstancesSerializer,
    StudySeriesInstancesSerializer,
)


class DocumentView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    parser_classes = (MultiPartParser, )
    filter_fields = (
        'patient_name', 'patient_id', 'study_instance_uid',
        'series_number', 'series_number', 'study_id'
    )
    http_method_names = ['get', 'post', 'head', 'options']


class StudiesListView(DocumentView):
    """ View to list all studies in the system. """

    queryset = distinct_studies = Document.objects.order_by(
        'study_id').distinct('study_id')
    serializer_class = StudiesSerializer


class SeriesListView(DocumentView):
    """ View to list all series in the. """

    serializer_class = StudySeriesSerializer
    http_method_names = ['get', 'head', 'options']


class InstancesListView(DocumentView):
    """ View to list all series in the. """

    serializer_class = StudyInstancesSerializer
    http_method_names = ['get', 'head', 'options']


class StudySeriesListView(StudiesListView):
    """ View to list all series in a study. """

    serializer_class = StudySeriesSerializer
    http_method_names = ['get', 'head', 'options']

    def get(self, request, study_id, format=None):

        queryset = Document.objects.filter(study_id=study_id)
        serializer = StudySeriesSerializer(queryset, many=True)
        return Response(serializer.data)


class StudyInstancesListView(StudiesListView):
    """ View to list all instances in a study. """

    serializer_class = StudyInstancesSerializer
    http_method_names = ['get', 'head', 'options']

    def get(self, request, study_id, format=None):

        queryset = Document.objects.filter(study_id=study_id)
        serializer = StudyInstancesSerializer(queryset, many=True)
        return Response(serializer.data)


class StudySeriesInstancesListView(StudiesListView):
    """ View to list all instances in a study. """

    serializer_class = StudySeriesInstancesSerializer
    http_method_names = ['get', 'head', 'options']

    def get(self, request, study_id, series_number, format=None):

        queryset = Document.objects.filter(
            study_id=study_id, series_number=series_number
        )
        serializer = StudySeriesInstancesSerializer(queryset, many=True)
        return Response(serializer.data)

# ---------------------------------------------------------------------- #
#                   | RETRIEVE VIEWS START HERE |                        #
# ---------------------------------------------------------------------- #


class RetrieveStudyView(generics.RetrieveAPIView):
    """ View to list all series in a study. """
    queryset = distinct_studies = Document.objects.order_by(
        'study_id').distinct('study_id')
    serializer_class = StudiesSerializer

    def retrieve(self, request, study_id, format=None):

        # for study in self.get_queryset():
        #     if study.study_id == study_id:
        #         self.queryset = study

        serializer = StudiesSerializer(self.get_queryset(), many=True)

        return Response(serializer.data)
