# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User



from django.db import models


# Create your models here.


class CommentSet(models.Model):
    pass


class Comment(models.Model):
    title = models.CharField("عنوان", default='', max_length=25)
    context = models.TextField("متن نظر")
    comment_set = models.ForeignKey('CommentSet', related_name='comments', unique=True)

    class Meta:
        verbose_name_plural = 'کامنت ها'
        verbose_name = 'کامنت'


class Rating(models.Model):
    tasker = models.ForeignKey('user.Member')
    customer = models.ForeignKey('user.Member', related_name='customer')
    rating = models.PositiveSmallIntegerField("نمره", default=0)

    class Meta:
        verbose_name_plural = 'امتیازها'
        verbose_name = 'امتیاز'

    def save(self, **kwargs):
        super(Rating, self).save()
