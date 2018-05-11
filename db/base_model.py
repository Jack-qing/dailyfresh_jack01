#!/usr/bin/python3 
# -*-coding:utf-8-*- 
# @Author: zhu shiqing
# @Time: 2018年05月01日17时45分 
# 说明: 
# 总结:
from django.db import models


class BaseModel(models.Model):
    '''模型抽象类'''
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:
        '''一个抽象模型类'''
        abstract = True