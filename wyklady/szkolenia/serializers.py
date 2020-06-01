from rest_framework import serializers
from .models import *


class UczestnicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Uczestnicy
        fields = '__all__'


class OrganizatorzySerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizatorzy
        fields = '__all__'


class SzkoleniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Szkolenia
        fields = '__all__'


class UczestnicySzkolenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UczestnicySzkolen
        fields = '__all__'
