from django.utils import timezone
from django.db import models


class Document(models.Model):
    """
    A storage for all the attachment

    Attachments include images(png, jpeg) and documents(pdf, excel, word)
    """
    title = models.CharField(max_length=255)
    data = models.FileField(upload_to='documents')
    upload_date = models.DateTimeField(editable=False)
    size = models.IntegerField(editable=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.upload_date = timezone.now()
        return super(Document, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
