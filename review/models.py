# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
# from user.models import Customer, Tasker


class Comment(models.Model):
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField("عنوان", default='', max_length=25)
    context = models.TextField("متن نظر")


class Rating(models.Model):
    # tasker = models.ForeignKey(Tasker)
    # customer = models.ForeignKey(Customer)
    kindness = models.PositiveSmallIntegerField("خوش رویی", default=0)
    speed = models.PositiveSmallIntegerField("سرعت عمل", default=0)
    performance = models.PositiveSmallIntegerField("کارایی", default=0)
    price = models.PositiveSmallIntegerField("قیمت مناسب", default=0)
