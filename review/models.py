# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from datetime import datetime
from django.db import models

# Create your models here.


class CommentSet(models.Model):
    def __str__(self):
        return str(self.id)


class DateMixin(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    def elapsed_time(self):
        time_delta = datetime.now() - self.date
        seconds = time_delta.seconds
        if seconds < 60:
            return "چند لحظه پیش"
        if seconds < 3600:
            return str(int(seconds / 60)) + " دقیقه پیش"
        if time_delta.days < 1:
            return str(int(seconds / 3600)) + " ساعت پیش"
        if time_delta.days < 365:
            return str(int(time_delta.days)) + " روز پیش"
        return self.date.date


class Comment(DateMixin):
    context = models.TextField("متن نظر")
    comment_set = models.ForeignKey('CommentSet', related_name='comments')
    author = models.ForeignKey('user.Member', related_name='comments')

    class Meta:
        verbose_name_plural = 'کامنت ها'
        verbose_name = 'کامنت'

    def __str__(self):
        return self.context


class Rate(models.Model):
    order = models.OneToOneField('service.Order', related_name='rate')
    customer = models.ForeignKey('user.Member', related_name='customer')  # todo inja afzoonegi darim
    rate = models.PositiveSmallIntegerField("نمره", default=0)

    class Meta:
        verbose_name_plural = 'امتیازها'
        verbose_name = 'امتیاز'

    def save(self, **kwargs):
        skill = self.order.skill
        skill_rate_num = skill.orders.filter(status='D').count()
        skill.rate = (skill_rate_num * skill.rate + self.rate) / (skill_rate_num + 1)
        skill.save()
        member = self.order.skill.tasker
        order_rate_count = member.get_done_sales_count()
        member.rate = (order_rate_count * member.rate + self.rate) / (order_rate_count + 1)
        member.save()
        super(Rate, self).save()
