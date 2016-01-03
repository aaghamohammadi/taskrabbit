from django.forms.models import ModelForm
from django import forms

from service.models import TaskModel

__author__ = 'garfild'


class EditTaskForm(ModelForm):
    name = forms.CharField(required=True, label='نام خدمت', widget=forms.TextInput(
        attrs={'class': 'required'}))
    image = forms.ImageField(required=True, label='عکس')

    class Meta:
        model = TaskModel
        fields = ['name', 'image', 'description']
        labels = {
            'description': 'شرح خدمت'
        }
