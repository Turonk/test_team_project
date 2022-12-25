from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=200,verbose_name=('Тема'),null=True,)
    description = models.TextField(verbose_name=('Описание'), blank=True, null=True, )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Тему'
        verbose_name_plural = 'Темы'
