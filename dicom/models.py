from django.utils import timezone
from django.db import models


class Document(models.Model):
    """
    A storage for all the attachment

    Attachments include images(png, jpeg) and documents(pdf, excel, word)
    """
    data = models.FileField(upload_to='documents')
    title = models.CharField(max_length=255)
    upload_date = models.DateTimeField(default=timezone.now)
    size = models.IntegerField(help_text='The size of the attachment in bytes')

    def __str__(self):
        return self.title
