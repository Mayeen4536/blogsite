
from django import forms
from django.forms import ModelForm, formsets
from django.forms.widgets import Widget

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'pic')

        widget = {
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
            'body': forms.Textarea(attrs = {'class': 'form-control'}),
            'pic': forms.TextInput(attrs = {'class': 'form-control'}),
        }

    