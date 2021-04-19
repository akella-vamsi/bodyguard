from django import forms
from .models import *


class ImageForm(forms.ModelForm):
    class Meta:
        model = Captured_Image
        fields = ['name', 'Main_Img']