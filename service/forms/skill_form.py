from django.forms.models import ModelForm
from django import forms
from django.forms.widgets import Select, Textarea

from service.models import Skill, Category

__author__ = 'garfild'


class SkillForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='دسته‌بندی',
                                      widget=Select(attrs={'class': 'browser-default'}))

    description = forms.CharField(widget=Textarea(attrs={'class': 'materialize-textarea'}),
                                  label='شرح خدمت')

    class Meta:
        model = Skill
        fields = '__all__'
        labels = {
            'title': 'عنوان',
            'description': 'شرح خدمت',
            'category': 'دسته‌بندی‌‌',
            'image': 'عکس'
        }
