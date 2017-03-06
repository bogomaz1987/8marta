import random
import string
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


wishes_status = (
    (0, 'Не готово'),
    (1, 'Готово')
)

def get_unique_code():
    return ''.join(random.sample(string.ascii_lowercase, 3))

class Girls(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=250)
    flour = models.SmallIntegerField(verbose_name='Этаж')
    code = models.CharField(
        verbose_name='Уникальный код',
        max_length=3,
        default=get_unique_code,
        db_index=True
    )

    class Meta:
        verbose_name = 'Довочка'
        verbose_name_plural = 'Девченки'

    def __str__(self):
        return self.fio


class Gifts(models.Model):
    name = models.CharField(verbose_name='Желание', max_length=250)
    description = models.CharField(verbose_name='Описание', max_length=250, default='')

    class Meta:
        verbose_name = 'Желание'
        verbose_name_plural = 'Желания'

    def __str__(self):
        return self.name


class Wishes(models.Model):
    girl = models.ForeignKey('Girls', related_name='girl')
    gift = models.ForeignKey('Gifts', related_name='gift')
    status = models.BooleanField(verbose_name='Статус', default=False)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)

    class Meta:
        unique_together = (('girl', 'gift'),)
        verbose_name = 'Зарезервированный заказ'
        verbose_name_plural = 'Зарезервированные заказы'
