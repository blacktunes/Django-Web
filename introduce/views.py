from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import *
from .serializers import *


def update_log(request):
    logs = UpdateLog.objects.filter().order_by('date_added')
    context = {'logs': logs}
    return render(request, 'update_log.html', context)


def about(request):
    abouts = About.objects.filter()
    context = {'abouts': abouts}
    return render(request, 'about.html', context)


def tip(request):
    tips = Tip.objects.filter()
    context = {'tips': tips}
    return render(request, 'tip.html', context)


@api_view(['GET', 'POST'])
def about_api(request):
    if request.method == 'GET':
        content = About.objects.all()
        serializer = AboutSerializer(content, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def gamename_api(request):
    if request.method == 'GET':
        content = GameName.objects.all()
        serializer = NameSerializer(content, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def update_log_api(request):
    if request.method == 'GET':
        content = UpdateLog.objects.all()
        serializer = UpdateLogSerializer(content, many=True)
        return Response(serializer.data)