from rest_framework import serializers

from webapp.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'name', 'file', 'creation_date', 'author', 'type', 'access_users')
