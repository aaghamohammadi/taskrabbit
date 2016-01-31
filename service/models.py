import random

from django.db import models

# Create your models here.
from review.models import CommentSet


class Skill(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    category = models.ForeignKey('Category', related_name='skills')
    price = models.IntegerField()
    image = models.ImageField(upload_to='skill_images')
    tasker = models.ForeignKey('user.Member', related_name='skills')
    comment_set = models.OneToOneField('review.CommentSet', related_name='skill')

    # todo bayad duration dashte bashe
    def __str__(self):
        return str(self.title) + " " + str(self.category)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.comment_set = CommentSet.objects.create()
        else:
            print(self.pk)
        super(Skill, self).save()


ORDER_STATUS = (
    ('S', 'معلق'),
    ('P', 'در حال انجام'),
    ('D', 'انجام شده')
)


class Order(models.Model):
    customer = models.ForeignKey('user.Member', related_name='orders')
    skill = models.ForeignKey('Skill', related_name='orders')
    code = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=1, choices=ORDER_STATUS, default='S', null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.code = random.randint(0, 1000000)
        super(Order, self).save()


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_images')

    def __str__(self):
        return self.name
        # todo bayad image ham dashte bashe
