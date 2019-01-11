# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models
# Create your models here.
#发布会表
class Event(models.Model):
    name=models.CharField(max_length=100)#发布会id
    limit=models.IntegerField()#参加人数
    status=models.BooleanField()#发布会的状态是否开启
    address=models.CharField(max_length=200)#发布会地点
    start_time=models.DateTimeField('events time')#发布会开始时间
    create_time=models.DateTimeField(auto_now=True)#创建时间
#当前时间
    def __str__(self):
        return self.name
#嘉宾表
class Guest(models.Model):
    event=models.ForeignKey(Event)#关联发布会标题
    realname=models.CharField(max_length=64)#姓名
    phone=models.CharField(max_length=16)#手机号
    email=models.EmailField()#邮箱
    sign=models.BooleanField()#签到状态
    create_time=models.DateTimeField(auto_now=True)#创建时间（自动获取当前时间）
class Meta:
    unique_together=("event","phone")
def __str__(self):
     return self.realname


