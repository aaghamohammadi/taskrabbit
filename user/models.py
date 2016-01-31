# Create your models here.
import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

from review.models import CommentSet

GENDER_CHOICES = (
    ('M', 'مرد'),
    ('F', 'زن'),
)


class Member(models.Model):
    user = models.OneToOneField(User, related_name='member')
    # username
    # password
    # email
    full_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=12)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M', null=True)
    city = models.CharField(max_length=25)
    address = models.CharField(max_length=150)
    # skills = models.ManyToManyField('service.Skill', related_name='member')
    image = models.ImageField(upload_to='profile_images', default='/static/images/user/profile-image-default.jpg')
    # confirmation
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today)
    comment_set = models.OneToOneField('review.CommentSet', related_name='member')
    credit = models.IntegerField(default=0)

    def get_score(self):
        return self.rating_set.aggregate(Sum('rating'))

    class Meta:
        verbose_name_plural = 'کاربران نوع مشتری'
        verbose_name = 'کاربر نوع مشتری'

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.pk:
            self.comment_set = CommentSet.objects.create()
        super(Member, self).save()


        #     birthday = models.jDateField()

# class Person(models.Model):
#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=25)
#     national_id = models.CharField(max_length=16)
#     home_number = models.CharField(max_length=12)
#     mobile_number = models.CharField(max_length=12)
#     birthday = models.DateField(blank=True, null=True)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
#     city = models.CharField(max_length=25, default='تهران')
#     district = models.CharField(max_length=25, default='تهران')
#
#     class Meta:
#         abstract = True
#
#
# class Customer(Person):
#     user = models.OneToOneField(User)
#     # username
#     # password
#     # email
#
#     class Meta:
#         verbose_name_plural = "کاربران نوع مشتری"
#         verbose_name = "کاربر نوع مشتری"
#
#     def __str__(self):
#         return self.user.username
#
#
# class Date(models.Model):
#     date = models.DateField()
#     time_choices = (
#         ('morning', 'صبح'),
#         ('noon', 'ظهر'),
#         ('afternoon', 'بعد از ظهر'),
#         ('full time', 'تمام وقت')
#     )
#     time = models.CharField(choices=time_choices, max_length=12)
#
#     def __str__(self):
#         return str(self.date)
#
#
# class Tasker(Person):
#     user = models.OneToOneField(User)
#     availability = models.ForeignKey(Date, null=True, blank=True)  # TODO bas doros she
#     # wage = models.IntegerField(default=0)
#     rate = models.IntegerField(default=0)
#
#     class Meta:
#         verbose_name_plural = "خدمت گزاران"
#         verbose_name = "خدمت گزار"
#
#     def __str__(self):
#         return self.person.first_name + " " + self.person.last_name
