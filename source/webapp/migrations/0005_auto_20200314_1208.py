# Generated by Django 2.2 on 2020-03-14 12:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_file_access_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='access_users',
            field=models.ManyToManyField(blank=True, null=True, related_name='file_access', to=settings.AUTH_USER_MODEL, verbose_name='группа'),
        ),
    ]