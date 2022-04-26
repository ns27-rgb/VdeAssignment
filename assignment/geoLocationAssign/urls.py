from django.urls import path, include
from . import views
from geoLocationAssign.views import *
from django.conf.urls import url, include

urlpatterns = [
    url(r'^getAddressDetails$',  views.getAddressDetails.as_view(), name='getAddressDetails'),
]