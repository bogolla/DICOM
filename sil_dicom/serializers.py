from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document


class StudiesSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):

        payload = {
            'study_id': obj.study_id,
            'patient_name': obj.patient_name,
            'patient_id': obj.patient_id,
            'patient_age': obj.patient_age,
            'series': [
                d.series_number for d in
                Document.objects.filter(study_id=obj.study_id)
            ],
            'instances': [
                d.study_instance_uid for d in
                Document.objects.filter(study_id=obj.study_id)
            ]
        }

        return payload

    class Meta:
        model = Document
