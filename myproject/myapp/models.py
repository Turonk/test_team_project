from django.db import models


class Invoice_position(models.Model):
    invoce_name = models.CharField(max_length=200,verbose_name=('Наименование по накладной'))
    invoce_number = models.CharField(max_length=50,verbose_name=('Номер накладной'))
    pub_data = models.DateTimeField(verbose_name=('Дата накладной'))
    count = models.IntegerField(default=1, verbose_name=('Количество'))
    stock_position = models.ForeignKey(
        Part,
        verbose_name="Позиция на складе",
        on_delete=models.CASCADE,
    )
    unit_price = models.IntegerField(default=1, verbose_name='Цена за единицу, руб')
    summa = models.IntegerField(default=1, verbose_name=('Сумма'))
    manufacturer = models.CharField(max_length=300, verbose_name=('Производитель'))

    def __str__(self):
        return self.manufacturer

    class Meta:
        verbose_name = 'Позиция по накладной'
        verbose_name_plural = 'Позиции по накладным'

class Topic(models.Model):
    title = models.CharField(max_length=200,verbose_name=('Тема'),null=True,)
    description = models.TextField(verbose_name=('Описание'), blank=True, null=True, )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Тему'
        verbose_name_plural = 'Темы'

