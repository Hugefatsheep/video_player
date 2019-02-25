# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'FatSheep'
__time__ = '2019/1/24'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗┃┃┃┃┃┃┃┃┃┃┃┃┃┃┓
                ┃  神兽保佑                       ┣┓
                ┃　                              ┏┛
                ┃　永无BUG！                     ┣┓
                ┃　    ┃┃┃┃┃┃┃┃┃┃┃    ┏┛
                ┗┓┓┏                    ┳┓┏┛ 
                  ┃┫┫                    ┃┫┫     
                  ┗┻┛                    ┗┻┛
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

]

