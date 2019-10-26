#coding=utf-8
from django.db import models

#定义地区模型类，存储省、市、区县信息
class AreaInfo(models.Model):
    atitle=models.CharField(max_length=30)#名称
    aParent=models.ForeignKey('self',null=True,blank=True)#父级


class PicTest(models.Model):
    pic = models.ImageField(upload_to='booktest/')