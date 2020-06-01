from django.contrib import admin

from .models import *


admin.site.register(Uczestnicy)
admin.site.register(Organizatorzy)
admin.site.register(Szkolenia)
admin.site.register(UczestnicySzkolen)
