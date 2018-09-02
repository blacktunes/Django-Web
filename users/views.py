from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from .forms import RegisterForm
import datetime

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth.models import User
from .serializers import *


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    if request.method != 'POST':
        form = RegisterForm()
    else:
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            successful = '<div class="alert alert-success"><a href="#" class="close" data-dismiss="alert">&times;</a><strong>注册成功!</strong> 并已为你自动登录</div>'
            return render(request, 'users/register.html', {"successful": successful})
        else:
            error_register = '<div class="alert alert-danger"><a href="#" class="close" data-dismiss="alert">&times;</a><strong>注册失败!</strong> 原因可能是用户名已被注册或者两次密码输入不相同</div>'
            return render(request, 'users/register.html', {"error_register": error_register})

    context = {'form': form}
    return render(request, 'users/register.html', context)


@api_view(['GET', 'POST'])
def user_api(request):
    # if request.method == 'GET':
    #     content = User.objects.all()
    #     serializer = UserSerializer(content, many=True)
    #     return Response(serializer.data)
    if request.method == 'POST':
        content = User.objects.all()
        serializer = UserSerializer(content, many=True)
        for i in serializer.data:
            if request.data['username'] == i['username']:
                authenticated_user = authenticate(username=request.data['username'], password=request.data['password'])
                if authenticated_user:
                    date = datetime.datetime.now()
                    User.objects.filter(username=request.data['username']).update(last_login=date)
                    return Response({'isLogin': True, 'userId': i['id']})
                else:
                    return Response('登录失败')
        return Response('无此用户')


@api_view(['GET', 'POST'])
def last_login_api(request):
    if request.method == 'POST':
        date = datetime.datetime.now()
        User.objects.filter(username=request.data['username']).update(last_login=date)
        return Response()