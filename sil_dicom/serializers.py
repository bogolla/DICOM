from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document


class StudiesSerializer(DocumentSerializer):

    def to_representation(self, obj):
        study_series = list(set(
            d.series_number for d in Document.objects.filter(
                study_id=obj.study_id)
        ))
        study_instances = list(set(
            d.study_instance_uid for d in
            Document.objects.filter(study_id=obj.study_id)
        ))

        payload = {
            'study_id': obj.study_id,
            'patient_name': obj.patient_name,
            'patient_id': obj.patient_id,
            'patient_age': obj.patient_age,
            # 'dicom_image': obj.data,
            'image_size': obj.image_size,
            'study_series': study_series,
            'study_instances': study_instances
        }

        return payload


class StudySeriesSerializer(DocumentSerializer):

    # TODO Bundle similar series into one and create one list for its instances
    def to_representation(self, obj):
        series_list = obj.series_number
        series_instances = obj.series_instance_uid

        payload = {
            'study_id': obj.study_id,
            'patient_name': obj.patient_name,
            'patient_id': obj.patient_id,
            # 'dicom_image': obj.data,
            'image_size': obj.image_size,
            'series_number': series_list,
            'series_instances': [series_instances]
        }

        return payload


class StudyInstancesSerializer(DocumentSerializer):

    # TODO Bundle similar series into one and create one list for its instances
    def to_representation(self, obj):

        study_instances = obj.study_instance_uid

        payload = {
            'study_id': obj.study_id,
            'patient_name': obj.patient_name,
            'patient_id': obj.patient_id,
            # 'dicom_image': obj.data,
            'image_size': obj.image_size,
            'study_instances_uid': study_instances
        }

        return payload


class StudySeriesInstancesSerializer(DocumentSerializer):

    # TODO Bundle similar series into one and create one list for its instances
    def to_representation(self, obj):
        series_instances = obj.series_instance_uid
        study_instances = obj.study_instance_uid
        series = obj.series_instance_uid

        payload = {
            'study_id': obj.study_id,
            'series_number': series,
            'patient_name': obj.patient_name,
            'patient_id': obj.patient_id,
            # 'dicom_image': obj.data,
            'image_size': obj.image_size,
            'series_instance': series_instances,
            'study_instance': study_instances
        }

        return payload
