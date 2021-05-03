from django.urls import path
from . import views
from django.conf import settings
from .views import *

urlpatterns = [

    path('live',livefe , name='live'),
    path('', views.home, name='home'),
    path('verify',views.verify,name='verify')
]
'''if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)'''