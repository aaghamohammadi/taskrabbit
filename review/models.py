# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models


# Create your models here.


class CommentSet(models.Model):
    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    context = models.TextField("متن نظر")
    comment_set = models.ForeignKey('CommentSet', related_name='comments')
    author = models.ForeignKey('user.Member', related_name='comments')

    class Meta:
        verbose_name_plural = 'کامنت ها'
        verbose_name = 'کامنت'

    def __str__(self):
        return self.context


class Rating(models.Model):
    tasker = models.ForeignKey('user.Member')
    customer = models.ForeignKey('user.Member', related_name='customer')
    rating = models.PositiveSmallIntegerField("نمره", default=0)

    class Meta:
        verbose_name_plural = 'امتیازها'
        verbose_name = 'امتیاز'

    def save(self, **kwargs):
        super(Rating, self).save()
