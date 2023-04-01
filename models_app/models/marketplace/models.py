# -*- coding: utf8 -*-
from django.db import models


class Marketplace(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        db_table = "marketplaces"
        verbose_name = 'Площадка'
        verbose_name_plural = 'Площадки'
