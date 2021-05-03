from django.shortcuts import render,redirect
from django.http import HttpResponse,StreamingHttpResponse,HttpResponseRedirect
from django.views.decorators import gzip
import cv2
import re
import base64
import numpy as np
import threading
from django.shortcuts import redirect
from .models import Captured_Image
from .forms import ImageForm


def home(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'capture/home.html',)


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()


    def __del__(self):
        self.video.release()


    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


@gzip.gzip_page
def livefe(request):
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
        pass



def verify(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Captured_Image(file_field=request.FILES['image'])
            instance.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = ImageForm()
    return render(request, 'success.html', {'form': form})

    '''dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
    ImageData = request.POST.get('hidden_image_field')
    ImageData = dataUrlPattern.match(ImageData).group(2)

    # If none or len 0, means illegal image data
    if (ImageData == None) or len(ImageData) == 0:
        pass

    # Decode the 64 bit string into 32 bit
    ImageData = base64.b64decode(ImageData)'''


def redirect_view(request):
    response = redirect('/capture/')
    return response