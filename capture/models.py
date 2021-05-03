from django.db import models


class Captured_Image(models.Model):
    name = models.CharField(max_length=50)
    main_image = models.FileField(upload_to='images/',default="")
# Create your models here.
