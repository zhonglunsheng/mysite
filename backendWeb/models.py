from django.db import models

# Create your models here.


class LoginUser(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True, verbose_name='用户id')
    user_name = models.CharField(max_length=30, null=False, blank=False, verbose_name='用户名')
    user_password = models.CharField(max_length=20, null=False, blank=False, verbose_name='用户密码')

    class Meta:
        verbose_name = '用户登录表',
        verbose_name_plural = verbose_name
        ordering = ['-user_id']
        db_table = 'login_user'
