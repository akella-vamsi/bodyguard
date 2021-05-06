from django import forms


class ImageForm(forms.Form):
    dataURL = forms.CharField()

