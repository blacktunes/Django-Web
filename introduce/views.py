from django.shortcuts import render
from .models import *


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
