from django.utils import timezone
from django.db import models


class Document(models.Model):
    """
    A storage for all the attachment

    Attachments include images(png, jpeg) and documents(pdf, excel, word)
    """
    data = models.FileField(upload_to='documents')
    title = models.CharField(max_length=255)
    upload_date = models.DateTimeField(editable=False)
    size = models.IntegerField(help_text='The size of the attachment in bytes')

    def save(self, *args, **kwargs):
        self.upload_date = timezone.now()
        return super(Document, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
