from django.forms.models import ModelForm
from django import forms
from django.forms.widgets import Select, Textarea, TextInput

from service.models import Skill, Category

__author__ = 'garfild'


class SkillForm(ModelForm):
    title = forms.CharField(widget=TextInput(attrs={'placeholder': 'من میتونم ...'}), label='عنوان')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='دسته‌بندی',
                                      widget=Select(attrs={'class': 'browser-default'}))

    description = forms.CharField(widget=Textarea(attrs={'class': 'materialize-textarea'}),
                                  label='شرح کامل خدمت')

    class Meta:
        model = Skill
        exclude = ['tasker', 'comment_set', 'rate']
        labels = {
            'category': 'دسته‌بندی‌‌',
            'price': 'قیمت',
            'image': 'عکس'
        }
