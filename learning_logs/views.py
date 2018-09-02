from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from .serializers import *



def index(request):
    return render(request, 'index.html')


@login_required()
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)


@login_required()
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', context)


@login_required()
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
        else:
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'new_topic.html', context)


@login_required()
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic_id]))
        else:
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'new_entry.html', context)


@login_required()
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'edit_entry.html', context)


@login_required()
def new_entry2(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.owner = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'new_entry2.html', context)


@login_required()
def edit_entry2(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'edit_entry2.html', context)


@login_required()
def del_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    Entry.objects.filter(id=entry_id).delete()
    return HttpResponseRedirect(reverse('learning_logs:topic',
                                        args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'edit_entry.html', context)


@api_view(['GET', 'POST'])
def topic_api(request):
    # if request.method == 'GET':
    #     content = Topic.objects.all()
    #     serializer = TopicSerializer(content, many=True)
    #     return Response(serializer.data)
    if request.method == 'POST':
        content = Topic.objects.filter(owner=request.data['userId']).order_by('date_added')
        serializer = TopicSerializer(content, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def entry_api(request):
    # if request.method == 'GET':
    #     content = Entry.objects.all()
    #     serializer = EntrySerializer(content, many=True)
    #     return Response(serializer.data)
    if request.method == 'POST':
        content = Entry.objects.filter(topic=request.data['topicId'])
        serializer = EntrySerializer(content, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def new_entry_api(request):
    # if request.method == 'GET':
    #     content = Entry.objects.all()
    #     serializer = EntrySerializer(content, many=True)
    #     return Response(serializer.data)
    if request.method == 'POST':
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def new_topic_api(request):
    # if request.method == 'GET':
    #     content = Topic.objects.all()
    #     serializer = TopicSerializer(content, many=True)
    #     return Response(serializer.data)
    if request.method == 'POST':
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)