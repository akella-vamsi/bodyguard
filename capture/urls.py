from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [

    path('live', live_feed, name='live'),
    path('', home, name='home'),
    path('verify', verify, name='verify'),
    path('success', success, name='success')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
