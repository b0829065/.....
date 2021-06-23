from django import http
from django.core import paginator
from django.core import serializers
from django.core.serializers import serialize
from django.db.models.lookups import PostgresOperatorLookup
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder, Serializer
from django.http import JsonResponse
from django.core.paginator import Page, Paginator,EmptyPage,PageNotAnInteger

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json

from .models import Post, User_login
from .models import User
# Create your views here.

class HelloAPIView(APIView):
    def get(self,request):
        get_name = request.GET.get('name',None)
        # logger.debug("**************** HelloAPIView : "+get_name)
        retValue = {}
        if get_name:
            retValue['data'] = "Hello " + get_name
            return Response(retValue,status=status.HTTP_200_OK)
        else:
            return Response(
                {"res":"ok"},
                status=status.HTTP_400_BAD_REQUEST
                )
class Add_user(APIView): #註冊
    def get(self,request):
        get_id = request.GET.get('user_id','')
        get_content = request.GET.get('content','')
        get_Stock_code = request.GET.get('Stock_code','')
        new_user = User_login()
        new_user.user_id = get_id
        new_user.content = get_content
        new_user.Stock_code = get_Stock_code
        new_user.save()
        if get_id:
            return JsonResponse({'data': get_id + ' insert!'},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)


class Delete_user(APIView): #刪除USER /deleteuser
    def get(self,request):
        get_id = request.GET.get('user_id','')
        user = User_login.objects.filter(user_id=get_id)
        user.delete()
        if get_id:
            return JsonResponse({'user ID:':get_id + ' delete!'},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)     


class Update_user(APIView): #更改帳密 or content/updateuser 
    def get(self,request):
        # get_id = request.GET.get('id','')
        get_userid=request.GET.get('user_id','')
        get_nickname = request.GET.get('nickname','')
        get_password = request.GET.get('password','')
        change_password = request.GET.get('changepassword','')
        update_user = User_login.objects.filter(user_id=get_userid,password=get_password)
        update_user.update(nickname=get_nickname,password=change_password)
        if get_userid:
            return JsonResponse({'user ID':get_userid + ' update!'},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)

class Login(APIView): #更改登入狀態/login
    def get(self,request):
        get_userid=request.GET.get('user_id','')
        get_password = request.GET.get('password','')
        login_check=request.GET.get('login_check','')
        update_user = User_login.objects.filter(user_id=get_userid,password=get_password)
        update_user.update(login_check=login_check)
        for e in User_login.objects.all():
            if(e.user_id==get_userid):
                nickname=e.nickname
        for i in User_login.objects.all():
            if(i.user_id==get_userid):
                id=i.id
        if update_user:
            if login_check==False:
                return JsonResponse({'User':get_userid + ' 已成功登出'},status=status.HTTP_200_OK)
            else: 
                return JsonResponse({'id':id ,'User':get_userid + '已成功登入','nickname':nickname},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)


class List_post(APIView):
    def get(self,request):
        page = request.GET.get('page',1) #  browsing page i
        posts = Post.objects.all().values()

        paginator = Paginator(posts,10) #10 data for one page
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return JsonResponse(
            # {'data':json.dumps(list(posts),sort_keys=True,indent=1,cls=DjangoJSONEncoder)},
            {'data':list(posts)},
            status=status.HTTP_200_OK
        )
class List_User(APIView):
    def get(self,request):
        user = User_login.objects.all().values()
        return JsonResponse(
            {'data':list(user)},
            status=status.HTTP_200_OK
        )