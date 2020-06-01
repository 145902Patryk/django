from rest_framework import viewsets
from .serializers import *
from rest_framework import permissions
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


class UczestnicyView(viewsets.ModelViewSet):
    queryset = Uczestnicy.objects.all()
    serializer_class = UczestnicySerializer
    permission_classes = [permissions.IsAdminUser]


class OrganizatorzyView(viewsets.ModelViewSet):
    queryset = Organizatorzy.objects.all()
    serializer_class = OrganizatorzySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SzkoleniaView(viewsets.ModelViewSet):
    queryset = Szkolenia.object.all()
    serializer_class = SzkoleniaSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class UczestnicySzkolenView(viewsets.ModelViewSet):
    queryset = UczestnicySzkolen.object.all()
    serializer_class = UczestnicySzkolenSerializer
    permission_classes = [permissions.IsAdminUser]


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
