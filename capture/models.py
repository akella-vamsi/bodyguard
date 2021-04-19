from django.db import models


class Captured_Image(models.Model):
    name = models.CharField(max_length=50)
    Main_Img = models.ImageField(upload_to='images/')
# Create your models here.
