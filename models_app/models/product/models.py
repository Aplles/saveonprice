# -*- coding: utf8 -*-
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    article = models.IntegerField(verbose_name="Артикул товара")
    image = models.ImageField(upload_to="products/", verbose_name="Изображение")
    price = models.IntegerField(verbose_name="Цена товара")
    presence = models.BooleanField(default=False, verbose_name="Наличие")
    receiving_price_changes = models.BooleanField(default=False, verbose_name="Отслеживать понижение стоимости")
    checking_presence = models.BooleanField(default=False, verbose_name="Отслеживать наличие товара")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    marketplace = models.ForeignKey(to='Marketplace', on_delete=models.CASCADE, related_name='marketplaces',
                                    verbose_name='Площадка')
    user = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name='users', verbose_name='Пользователь')

    class Meta:
        db_table = "products"
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
