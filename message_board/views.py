from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import MessageBoard
from .forms import MessageBoardForm


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
