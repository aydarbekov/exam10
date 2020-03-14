from django.db import models

TYPE_CHOICES = (
    ('general', 'Общий'),
    ('hidden', 'Скрытый'),
    ('private', 'Приватный'),
)

class File(models.Model):
    name = models.TextField(max_length=2000, verbose_name='Подпись')
    file = models.FileField(upload_to='files', verbose_name='Файл')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    author = models.ForeignKey('auth.User', related_name='file', on_delete=models.SET_NULL, null=True, blank=True,  verbose_name='автор')
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default=TYPE_CHOICES[0][0],
                                verbose_name='Тип')
    access_users = models.ManyToManyField('auth.User', null=True, blank=True, related_name='file_access', verbose_name='группа')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'