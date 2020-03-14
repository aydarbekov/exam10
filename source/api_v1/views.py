from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS

from api_v1.serializers import FileSerializer
from webapp.models import File


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    # def get_permissions(self):
    #     if self.request.method in SAFE_METHODS:
    #         return []
    #     return super().get_permissions()
