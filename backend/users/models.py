from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    patronymic = models.CharField(max_length=255, null=True,
                                  verbose_name='Отчество', blank=True)
    image = models.ImageField(verbose_name='Ваше изображение',
                              upload_to='images', null=True, blank=True)
    is_company = models.BooleanField(verbose_name='Являеться компаний',
                                     default=False)
    number = models.BigIntegerField(unique=True, null=False, default=0,
                                    verbose_name='Номер телефона')

