from django import forms

from webapp.models import File

class FileFormFullFull(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file', 'type', 'access_users']


class FileFormFull(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file', 'type']


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file']

class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")