# Generated by Django 2.2 on 2020-03-14 10:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0003_auto_20200314_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='access_users',
            field=models.ManyToManyField(related_name='file_access', to=settings.AUTH_USER_MODEL, verbose_name='группа'),
        ),
    ]
