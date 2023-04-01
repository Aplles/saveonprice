# -*- coding: utf8 -*-
from django.db import models


class History(models.Model):
    price = models.IntegerField(verbose_name="Цена товара")
    date = models.DateField(verbose_name="Дата")
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE, related_name='products', verbose_name='Продукт')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        db_table = "histories"
        verbose_name = 'История'
        verbose_name_plural = 'Истории'
