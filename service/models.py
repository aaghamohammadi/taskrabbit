from django.db import models

# Create your models here.


class Skill(models.Model):
    tasker = models.ForeignKey('user.Tasker', related_name='tasks')
    task_model = models.ForeignKey('TaskModel')
    salary = models.IntegerField()

class TaskModel(models.Model):
    name = models.CharField(max_length=50)
    # category = models.ForeignKey('Category')


class Order(models.Model):
    customer = models.ForeignKey('user.Customer')
    skill = models.ForeignKey('Skill')


class Category(models.Model):
    name = models.CharField(max_length=50)
