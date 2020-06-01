from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from .views import *
from django.contrib.auth import login

router = routers.DefaultRouter()
router.register('uczestnicy', views.UczestnicyView)
router.register('organizatorzy', views.OrganizatorzyView)
router.register('szkolenia', views.SzkoleniaView)
router.register('uczestnicyszkolen', views.UczestnicySzkolenView)

urlpatterns = [
    path('api/', include(router.urls)),
]
