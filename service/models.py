from django.db import models


# Create your models here.
from review.models import CommentSet


class Skill(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    category = models.ForeignKey('Category', related_name='skills')
    image = models.ImageField(upload_to='skill_images')
    tasker = models.ForeignKey('user.Member', related_name='skills')
    comment_set = models.OneToOneField('review.CommentSet', related_name='skill')
    price = models.IntegerField()

    # todo bayad duration dashte bashe
    def __str__(self):
        return str(self.title) + " " + str(self.category)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.comment_set = CommentSet.objects.create()
        else:
            print(self.pk)
        super(Skill, self).save()


class OrderBasket(models.Model):
    customer = models.ForeignKey('user.Member', related_name='baskets')


class Order(models.Model):
    basket = models.ForeignKey('user.Member', related_name='orders')
    skill = models.ForeignKey('Skill', related_name='orders')


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        # todo bayad image ham dashte bashe
