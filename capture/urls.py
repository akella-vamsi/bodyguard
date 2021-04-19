from django.urls import path
from . import views
from django.conf import settings
from .views import *

urlpatterns = [

    path('image_upload', image_view, name='image_upload'),
    path('success', success, name='success'),
    path('live',livefe , name='live'),
    path('', views.home, name='home'),
]
'''if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)'''