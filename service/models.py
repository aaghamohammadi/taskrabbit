from django.db import models

# Create your models here.


class Task(models.Model):
    tasker = models.ForeignKey('user.Tasker', related_name='tasks')
    task_model = models.ForeignKey('TaskModel')


class TaskModel(models.Model):
    name = models.CharField(max_length=50)
    # category = models.ForeignKey('Category')


class Order(models.Model):
    customer = models.ForeignKey('user.Customer')
    task = models.ForeignKey('Task')


class Category(models.Model):
    name = models.CharField(max_length=50)
