from django.db import models


# Create your models here.

class Skill(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    category = models.ForeignKey('Category', related_name='skills')
    image = models.ImageField(upload_to='skill_images')

    # todo bayad image dashte bashe
    def __str__(self):
        return str(self.title) + " " + str(self.category)


class Order(models.Model):
    customer = models.ForeignKey('user.Member')
    skill = models.ForeignKey('Skill')


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        # todo bayad image ham dashte bashe
