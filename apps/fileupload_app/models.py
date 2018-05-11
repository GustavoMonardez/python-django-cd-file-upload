from django.db import models
from django.conf import settings

class ModelWithFileField(models.Model):
    uploadedImage = models.FileField(upload_to=settings.MEDIA_ROOT)

