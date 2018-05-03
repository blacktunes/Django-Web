from django import forms

from .models import MessageBoard


class MessageBoardForm(forms.ModelForm):
    class Meta:
        model = MessageBoard
        fields = ['name', 'text']