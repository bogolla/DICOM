# stdlib
from datetime import datetime
import os

# 3rd Party
import dicom
from django.utils import timezone
from django.db import models

# project
from django.conf import settings


class DicomParsingException(Exception):
    """ Thrown when a file is unable to be parsed by the dicom library. """
    pass


class DicomPILException(Exception):
    """ Throwing if we're unable to convert a Dicom pixel array to PIL. """
    pass


class Document(models.Model):
    """ A model representation of an attachment (dicom file). """
    title = models.CharField(max_length=255)
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
        self.patient_name = dicom_obj.PatientName
        self.patient_id = dicom_obj.PatientID
        self.patient_age = dicom_obj.PatientAge
        self.study_date = datetime.strptime(
            dicom_obj.StudyDate, "%Y%m%d").date()
        self.image_size = len(dicom_obj.PixelData)
        self.body_part_examined = dicom_obj.BodyPartExamined
        self.study_description = dicom_obj.StudyDescription
        self.study_id = dicom_obj.StudyID
        self.study_instance_uid = dicom_obj.StudyInstanceUID
        self.series_number = dicom_obj.SeriesNumber
        self.series_instance_uid = dicom_obj.SeriesInstanceUID
        self.upload_date = timezone.now()

        # purge duplicate images from disc
        # self.purge_files()

        return super(Document, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
