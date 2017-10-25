from django.db import models
from django.utils import timezone


class Organization(models.Model):
    name = models.CharField(verbose_name='Название', max_length=64, unique=True)
    region = models.CharField(verbose_name='Регион', max_length=32)
    tax_id = models.IntegerField(verbose_name='ИНН')
    site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)


class Work(models.Model):
    organization = models.ForeignKey(Organization, verbose_name='Организация')
    position = models.CharField(verbose_name='Должность', max_length=64)
    duties = models.TextField(verbose_name='Обязанности')
    start = models.DateField(verbose_name='Начало')
    end = models.DateField(verbose_name='Конец', default=timezone.now)


class Education(models.Model):
    university = models.CharField(verbose_name='Учебное заведение', max_length=64)
    site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    department = models.CharField(verbose_name='Факультет', max_length=32, blank=True)
    speciality = models.CharField(verbose_name='Специальность', max_length=64)
    start = models.DateField(verbose_name='Начало')
    end = models.DateField(verbose_name='Конец', default=timezone.now)
