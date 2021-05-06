from django.shortcuts import render,redirect
from django.http import HttpResponse,StreamingHttpResponse,HttpResponseRedirect
from django.views.decorators import gzip
import cv2,json
import re
import base64
import numpy as np
import threading
from django.shortcuts import redirect
from .models import Captured_Image
from .forms import ImageForm

def home(request):
    return render(request, 'capture/home.html')


class Cam(object):
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
def live_feed(request):
    cam = Cam()
    return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    pass


def verify(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        ImageData = json.loads(body_unicode)

    # If none or len 0, means illegal image data
    if (ImageData == None) or len(ImageData) == 0:
        pass
    # Decode the 64 bit string into 32 bit
    ImageData = base64.b64decode(ImageData['imageData'])
    filename = 'Receive.png'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(ImageData)
        instance= Captured_Image()
        instance.save()
    return render(request,'capture/success.html')
def success(request):
    return render(request, 'capture/success.html',)
