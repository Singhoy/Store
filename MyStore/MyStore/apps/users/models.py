from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """
    用户信息
    """
    mobile = models.CharField(max_length=15, unique=True, verbose_name='手机号码')

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name