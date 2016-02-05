# Create your models here.
import datetime

from django.contrib.auth.models import User
from django.db import models

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
    # image = models.ImageField(upload_to='profile_images', default='/static/images/user/profile-image-default.jpg')
    image = models.ImageField(upload_to='profile_images', default='/media/profile_images/profile-image-default.jpg')

    # confirmation
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today)
    comment_set = models.OneToOneField('review.CommentSet', related_name='member')
    credit = models.IntegerField(default=0)

    def get_score(self):
        return self.orders.count()

    class Meta:
        verbose_name_plural = 'کاربران نوع مشتری'
        verbose_name = 'کاربر نوع مشتری'

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.pk:
            self.comment_set = CommentSet.objects.create()
        super(Member, self).save()
