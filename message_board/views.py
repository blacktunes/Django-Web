from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import *
from .forms import MessageBoardForm
from .serializers import *


def message_board(request):
    if request.method != 'POST':
        form = MessageBoardForm()
    else:
        form = MessageBoardForm(request.POST)
        if form.is_valid():
            message_board = form.save(commit=False)
            message_board.save()
            return HttpResponseRedirect(reverse('message_board:message_board'))

    message_board_list = MessageBoard.objects.filter()
    context = {'form': form,
               'message_board_list': message_board_list}

    return render(request, 'message_board.html', context)


@api_view(['GET', 'POST'])
def message_board_api(request):
    if request.method == 'GET':
        content = MessageBoard.objects.all()
        serializer = MesSerializer(content, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
