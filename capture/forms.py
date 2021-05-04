from django import forms


class ImageForm(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.FileField()
    hidden_image_field=forms.CharField()