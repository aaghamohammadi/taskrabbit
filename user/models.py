# Create your models here.

from django.contrib.auth.models import User
from django.db import models

GENDER_CHOICES = (
    ('M', 'مرد'),
    ('F', 'زن'),
)


class Customer(models.Model):
    user = models.OneToOneField(User)
    # username
    # password
    # email
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    national_id = models.CharField(max_length=16)
    home_number = models.CharField(max_length=12)
    mobile_number = models.CharField(max_length=12)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank="False")
    city = models.CharField(max_length=25, default='تهران')
    district = models.CharField(max_length=25, default='تهران')

    class Meta:
        verbose_name_plural = "کاربران نوع مشتری"
        verbose_name = "کاربر نوع مشتری"

    def __str__(self):
        return self.user.username


class Date(models.Model):
    date = models.DateField()
    time_choices = (
        ('morning', 'صبح'),
        ('noon', 'ظهر'),
        ('afternoon', 'بعد از ظهر'),
        ('full time', 'تمام وقت')
    )
    time = models.CharField(choices=time_choices, max_length=12)

    class Meta:
        verbose_name_plural = "روزها"
        verbose_name = "روز"

    def __str__(self):
        return str(self.date)


class Availability(models.Model):
    dates = models.ForeignKey(Date)

    class Meta:
        verbose_name_plural = "زمان های در دسترس"
        verbose_name = "زمان در دسترس"

    def __str__(self):
        return str(self.dates)


class Tasker(models.Model):
    person = models.OneToOneField(Customer)
    availability = models.ForeignKey(Availability)
    wage = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "خدمت گزاران"
        verbose_name = "خدمت گزار"

    def __str__(self):
        return self.person.first_name + " " + self.person.last_name

# class IntegerRangeField(models.IntegerField):
#   def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
#       self.min_value, self.max_value = min_value, max_value

#        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
#    def formfield(self, **kwargs):
#        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
#       defaults.update(kwargs)

# return super(IntegerRangeField, self).formfield(**defaults)

# class Rating(models.Model):
#     tasker = models.ForeignKey(Tasker)
#     person = models.ForeignKey(Person)
#     rating = models.IntegerRangeField(range(1, 5))
#
# class Comment(models.Model):
#     context = models.TextField(default='')
#     person = models.ForeignKey(Person)
#
