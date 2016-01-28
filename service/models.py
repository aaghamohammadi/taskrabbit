from django.db import models


# Create your models here.

class Skill(models.Model):
    category = models.ForeignKey('Category', related_name='skills')
    #todo bayad image dashte bashe


class Order(models.Model):
    customer = models.ForeignKey('user.Member')
    skill = models.ForeignKey('Skill')


class Category(models.Model):
    name = models.CharField(max_length=50)
    # todo bayad image ham dashte bashe
