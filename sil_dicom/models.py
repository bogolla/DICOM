# stdlib
from datetime import datetime
import os

# 3rd Party
import dicom
from django.utils import timezone
from django.db import models

# project
from django.conf import settings


CONTENT_TYPE = (
    ("image/dcm", "DCM"),
    ("image/png", "PNG"),
    ("image/jpeg", "JPEG"),
)


class DicomParsingException(Exception):
    """ Thrown when a file is unable to be parsed by the dicom library. """
    pass


class Document(models.Model):
    """ A model representation of an attachment (dicom file). """
    title = models.CharField(max_length=255)
    content_type = models.CharField(
        max_length=100, choices=CONTENT_TYPE, default='DCM')
    data = models.FileField(upload_to='documents')
    upload_date = models.DateTimeField(editable=False)

    # Fields extracted from the DICOM images
    image_size = models.CharField(editable=False, max_length=255)
    patient_name = models.CharField(editable=False, max_length=255)
    patient_id = models.CharField(editable=False, max_length=14)
    patient_age = models.CharField(editable=False, max_length=14)
    body_part_examined = models.CharField(editable=False, max_length=255)
    study_date = models.DateTimeField(editable=False)

    # Dicom image attributes (Study, Series and Instances)
    study_description = models.CharField(editable=False, max_length=255)
    study_id = models.CharField(editable=False, max_length=255)
    study_instance_uid = models.CharField(editable=False, max_length=255)
    series_number = models.CharField(editable=False, max_length=255)
    series_instance_uid = models.CharField(editable=False, max_length=255)

    def purge_files(self):
        """ Purge static files from the disk. """
        if self.data:
            img_path = os.path.join(
                settings.MEDIA_URL, 'documents', self.data)
            os.remove(img_path)

    def save(self, *args, **kwargs):
        # create the dicom image object to manipulate the image
        try:
            dicom_obj = dicom.read_file(self.data)
        except Exception:
            raise DicomParsingException(str(self.data))

        # use dicom attributes to populate model fields
        self.patient_name = str(getattr(dicom_obj, 'PatientName', 'Unknown'))
        self.patient_id = str(getattr(dicom_obj, 'PatientID', 'Unknown'))
        self.patient_age = str(getattr(dicom_obj, 'PatientAge', 'Unknown'))
        self.study_date = datetime.strptime(
            dicom_obj.StudyDate, "%Y%m%d").date()
        self.image_size = len(dicom_obj.PixelData)
        self.body_part_examined = str(
            getattr(dicom_obj, 'BodyPartExamined', 'Unknown'))
        self.study_description = str(
            getattr(dicom_obj, 'StudyDescription', 'Unknown'))
        self.study_id = str(getattr(dicom_obj, 'StudyID', 'Unknown'))
        self.study_instance_uid = str(
            getattr(dicom_obj, 'StudyInstanceUID', 'Unknown'))
        self.series_number = str(
            getattr(dicom_obj, 'SeriesNumber', 'Unknown'))
        self.series_instance_uid = str(
            getattr(dicom_obj, 'SeriesInstanceUID', 'Unknown'))
        self.upload_date = timezone.now()

        # purge duplicate images from disc
        # self.purge_files()

        return super(Document, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

UPS_STATUS = (
    ("created", "CREATED"),
    ("progress", "IN PROGRESS"),
    ("complete", "COMPLETE"),
    ("pending", "PENDING"),
    ("rejected", "REJECTED"),
)


class UnifiedProcedureStep(models.Model):
    patient_name = models.CharField(max_length=128)
    accession_number = models.CharField(max_length=128)
    requested_procedure_id = models.CharField(max_length=128)
    requested_procedure_desc = models.TextField()
    scheduled_station_AE_title = models.CharField(max_length=128)
    scheduled_ups_desc = models.TextField()
    ups_status = models.CharField(
        max_length=128, choices=CONTENT_TYPE, default='CREATED')

    def serialize_hook(self, hook):
        return {
            'hook': hook.dict(),
            'data': {
                'id': self.id,
                'patient_name': self.patient_name,
                'accession_number': self.accession_number,
                'requested_procedure_id': self.requested_procedure_id,
                'requested_procedure_desc': self.requested_procedure_desc,
                'scheduled_station_AE_title': self.scheduled_station_AE_title,
                'scheduled_ups_desc': self.scheduled_ups_desc,
                'ups_status': self.ups_status
            }
        }

    def mark_as_created(self):
        from rest_hooks.signals import hook_event
        hook_event.send(
            sender=self.__class__,
            action='created',
            instance=self # the Book object
        )
