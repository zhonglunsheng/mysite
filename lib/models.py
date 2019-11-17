from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    pub_house = models.CharField(max_length=1000)
    pub_date = models.DateField('出版时间')

