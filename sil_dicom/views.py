from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import viewsets
from rest_hooks.models import Hook

from .models import Document
from .serializers import (
    DocumentSerializer,
    StudiesSerializer,
    StudySeriesSerializer,
    StudyInstancesSerializer,
    StudySeriesInstancesSerializer,

    HookSerializer,
)


def distinct_series(key, val, lst):
    try:
        return next(filter(lambda elt: elt[key] == val, lst))
    except:
        return {"detail": "Not found."}


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

    queryset = Document.objects.order_by('study_id').distinct('study_id')
    serializer_class = StudiesSerializer


class SeriesListView(DocumentView):
    """ View to list all series in the. """

    serializer_class = StudySeriesSerializer
    http_method_names = ['get', 'head']

    def get(self, request, format=None):

        queryset = self.get_queryset()
        serializer = StudySeriesSerializer(queryset, many=True)

        base_obj = serializer.data

        series_arr = list(set(
            data['series_number'] for data in base_obj
        ))

        distinct_obj = map(lambda val: distinct_series(
            'series_number', val, base_obj), series_arr)

        return Response(distinct_obj)


class InstancesListView(DocumentView):
    """ View to list all series in the. """

    serializer_class = StudyInstancesSerializer
    http_method_names = ['get', 'head']


class StudySeriesListView(StudiesListView):
    """ View to list all series in a study. """

    serializer_class = StudySeriesSerializer
    http_method_names = ['get', 'head']

    def get(self, request, study_id, format=None):

        queryset = Document.objects.filter(study_id=study_id)
        serializer = StudySeriesSerializer(queryset, many=True)

        base_obj = serializer.data

        series_arr = list(set(
            data['series_number'] for data in base_obj
        ))

        distinct_obj = map(lambda val: distinct_series(
            'series_number', val, base_obj), series_arr)

        return Response(distinct_obj)


class StudyInstancesListView(StudiesListView):
    """ View to list all instances in a study. """

    serializer_class = StudyInstancesSerializer
    http_method_names = ['get', 'head']

    def get(self, request, study_id, format=None):

        queryset = Document.objects.filter(study_id=study_id)
        serializer = StudyInstancesSerializer(queryset, many=True)
        return Response(serializer.data)


class StudySeriesInstancesListView(StudiesListView):
    """ View to list all instances in a study. """

    serializer_class = StudySeriesInstancesSerializer
    http_method_names = ['get', 'head']

    def get(self, request, study_id, series_number, format=None):

        queryset = Document.objects.filter(
            study_id=study_id, series_number=series_number
        )
        serializer = StudySeriesInstancesSerializer(queryset, many=True)
        base_obj = serializer.data

        instance_arr = list(set(
            data['series_instance'] for data in base_obj
        ))

        distinct_obj = map(lambda val: distinct_series(
            'series_instance', val, base_obj), instance_arr)

        return Response(distinct_obj)

# ---------------------------------------------------------------------- #
#                   | RETRIEVE VIEWS START HERE |                        #
# ---------------------------------------------------------------------- #


class RetrieveStudyView(generics.RetrieveAPIView):
    """ View to retrive a study. """
    queryset = Document.objects.order_by('study_id').distinct('study_id')
    serializer_class = StudiesSerializer
    lookup_field = 'study_id'


class RetrieveStudySeriesView(RetrieveStudyView):
    """ View to retrive a series in a study. """
    queryset = Document.objects.order_by('study_id').distinct('study_id')
    serializer_class = StudySeriesSerializer

    def get(self, request, study_id, series_number, format=None):

        queryset = Document.objects.filter(study_id=study_id)
        serializer = StudySeriesSerializer(queryset, many=True)

        base_obj = serializer.data

        distinct_obj = map(lambda val: distinct_series(
            'series_number', val, base_obj), [series_number])

        return Response(distinct_obj)


class RetrieveStudySeriesInstanceView(generics.RetrieveAPIView):
    """ View to retrive a study. """
    queryset = Document.objects.order_by('study_id').distinct('study_id')
    serializer_class = StudiesSerializer

    def get(self, request, study_id, series_number, instance_uid, format=None):

        queryset = Document.objects.filter(
            study_id=study_id, series_number=series_number)
        serializer = StudySeriesSerializer(queryset, many=True)

        base_obj = serializer.data

        distinct_obj = map(lambda val: distinct_series(
            'series_instance_uid', val, base_obj), [instance_uid])

        return Response(distinct_obj)

# --------------------------Unified Procedure Step--------------------------- #
class HookViewSet(viewsets.ModelViewSet):
    """
    Retrieve, create, update or destroy webhooks.
    """
    model = Hook
    serializer_class = HookSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
