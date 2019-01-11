# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import  auth
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from sign.models import Event
def index(request):
    return  render(request,"index.html")
def login_action(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        #print username
        password=request.POST.get('password','') #获取不到数据返回为空
        #print password
        # if username=='admin' and password=='admin123':
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)#登录
            #return HttpResponse('login sucess')
            request.session['user'] = username  # 将session信息记录到浏览器
            response=HttpResponseRedirect('/event_manage/')#重定向url
            #response.set_cookie('user',username,3600)#添加浏览器cookie设置key,value

            return  response

        else:
            return  render(request,'index.html',{"error":'username or password error!'})
    else:
        return HttpResponse('must  post of method')
#发布会管理
@login_required
def event_manage(request):
    username=request.session.get('user','')#读取浏览器cookie
    # username=request.COOKIES.get('user','')#读取浏览器cookie
    return render(request,"event_manage.html",{"user":username})

