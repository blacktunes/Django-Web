from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from .forms import RegisterForm

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
