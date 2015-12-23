from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.forms import fields


class Person(models.Model):
    user = models.OneToOneField(User)
    # user name
    # password
    # Email
    nationalID = models.CharField(parimay_key=True, null=False, max_length=10)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=12)
    address = models.TextField(default='')
    # province = models.CharField(max_length=25, default='')
    city = models.CharField(max_length=25, default='')

    def __str__(self):
        return self.user.username


class Tasker(models.Model):
    person = models.OneToOneField(Person)
    availability = models.ForeignKey(Availability)
    wage = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)


class Availability(models.Model):
    dates = models.ForeignKey(Date)


class Date(models.Model):
    date = models.DateField(default='')
    time_choices = (
        ('morning', '???'),
        ('noon', '???'),
        ('afternoon', '??? ?? ???'),
        ('full time', '???? ???')
    )
    time = models.CharField(choices=time_choices, max_length=12)


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


# class Rating(models.Model):
#     tasker = models.ForeignKey(Tasker)
#     person = models.ForeignKey(Person)
#     rating = models.IntegerRangeField(range(1, 5))
#
# class Comment(models.Model):
#     context = models.TextField(default='')
#     person = models.ForeignKey(Person)
#