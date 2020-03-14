from django.db import models


class File(models.Model):
    name = models.TextField(max_length=2000, verbose_name='Подпись')
    file = models.FileField(upload_to='files', verbose_name='Файл')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    author = models.ForeignKey('auth.User', related_name='ads', on_delete=models.SET_NULL, null=True, blank=True,  verbose_name='автор')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'